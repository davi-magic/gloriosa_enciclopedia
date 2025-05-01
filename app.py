
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict

def extrair_dados_statistics(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')

        tabelas = soup.find_all('table')
        if not tabelas or len(tabelas) < 1:
            raise ValueError("Nenhuma tabela encontrada. Certifique-se de usar o link da aba 'Estatísticas' do Challenge Place.")

        jogadores = defaultdict(lambda: {"gols": 0, "assist": 0})

        for tabela in tabelas:
            cabecalho = [th.text.strip().lower() for th in tabela.find_all('th')]
            linhas = tabela.find_all('tr')[1:]

            for linha in linhas:
                colunas = linha.find_all('td')
                if len(colunas) < 2:
                    continue

                nome = colunas[1].text.strip()
                if "gols" in cabecalho:
                    try:
                        idx_gols = cabecalho.index("gols")
                        gols = int(colunas[idx_gols].text.strip())
                        jogadores[nome]["gols"] += gols
                    except:
                        pass
                if "assistências" in cabecalho or "assistencias" in cabecalho:
                    try:
                        idx_assist = cabecalho.index("assistências") if "assistências" in cabecalho else cabecalho.index("assistencias")
                        assist = int(colunas[idx_assist].text.strip())
                        jogadores[nome]["assist"] += assist
                    except:
                        pass
        return jogadores
    except Exception as e:
        st.error(f"Erro ao extrair dados de {link}: {e}")
        return {}

def consolidar_dados(temporadas):
    consolidados = defaultdict(lambda: {"gols": 0, "assist": 0})
    for temporada in temporadas:
        for jogador, stats in temporada.items():
            consolidados[jogador]["gols"] += stats["gols"]
            consolidados[jogador]["assist"] += stats["assist"]
    return consolidados

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
st.markdown("👉 **Cole abaixo os links da aba 'Estatísticas' dos torneios no Challenge Place.** Um por linha.")

links_texto = st.text_area("Links das temporadas")
temporadas = []

if st.button("Carregar Temporadas") and links_texto.strip():
    links = links_texto.strip().splitlines()
    with st.spinner("Extraindo dados..."):
        for link in links:
            dados = extrair_dados_statistics(link)
            if dados:
                temporadas.append(dados)
        st.success(f"{len(temporadas)} temporadas carregadas com sucesso.")

banco = consolidar_dados(temporadas) if temporadas else {}

pergunta = st.text_input("Faça sua pergunta (ex: Quem é o maior artilheiro da história?)")
if pergunta:
    resposta = responder(pergunta, banco)
    st.write(resposta)
