
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict

# Função para extrair dados de uma temporada
def extrair_dados_temporada(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        tabela = soup.find('table')
        linhas = tabela.find_all('tr')[1:]

        jogadores = defaultdict(lambda: {"gols": 0, "assist": 0})

        for linha in linhas:
            colunas = linha.find_all('td')
            if len(colunas) < 5:
                continue
            nome = colunas[1].text.strip()
            gols = int(colunas[3].text.strip())
            assist = int(colunas[4].text.strip())

            jogadores[nome]["gols"] += gols
            jogadores[nome]["assist"] += assist

        return jogadores
    except Exception as e:
        st.error(f"Erro ao extrair dados: {e}")
        return {}

# Função para somar os dados de todas as temporadas
def consolidar_dados(temporadas):
    consolidados = defaultdict(lambda: {"gols": 0, "assist": 0})
    for temporada in temporadas:
        for jogador, stats in temporada.items():
            consolidados[jogador]["gols"] += stats["gols"]
            consolidados[jogador]["assist"] += stats["assist"]
    return consolidados

# Função para responder perguntas
def responder(pergunta, banco):
    if not banco:
        return "Nenhum dado carregado ainda."

    df = pd.DataFrame([
        {"jogador": nome, "gols": stats["gols"], "assist": stats["assist"],
         "participacoes": stats["gols"] + stats["assist"]}
        for nome, stats in banco.items()
    ])

    pergunta = pergunta.lower()
    if "artilheiro" in pergunta or "mais gols" in pergunta:
        top = df.sort_values("gols", ascending=False).iloc[0]
        return f"O maior artilheiro é {top.jogador} com {top.gols} gols."
    elif "assistência" in pergunta or "assistencias" in pergunta:
        top = df.sort_values("assist", ascending=False).iloc[0]
        return f"O maior assistente é {top.jogador} com {top.assist} assistências."
    elif "participa" in pergunta or "gols + assist" in pergunta or "diretamente" in pergunta:
        top = df.sort_values("participacoes", ascending=False).iloc[0]
        return (f"O jogador com mais participações diretas em gols é {top.jogador} "
                f"com {top.participacoes} (gols + assistências).")
    else:
        return "Pergunta não reconhecida. Tente algo como 'Quem é o maior artilheiro?'"


st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="centered")
st.title("A Gloriosa Enciclopédia")
st.write("Cole abaixo os links das temporadas para extrair os dados.")

links = st.text_area("Cole os links do Challenge Place (um por linha):").strip().splitlines()
temporadas = []
if st.button("Carregar Temporadas"):
    with st.spinner("Extraindo dados..."):
        for link in links:
            dados = extrair_dados_temporada(link)
            if dados:
                temporadas.append(dados)
        st.success(f"{len(temporadas)} temporadas carregadas com sucesso.")

banco = consolidar_dados(temporadas) if temporadas else {}

pergunta = st.text_input("Faça sua pergunta (ex: Quem é o maior artilheiro da história?)")
if pergunta:
    resposta = responder(pergunta, banco)
    st.write(resposta)
