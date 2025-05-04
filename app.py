import streamlit as st
import pandas as pd
import re
from io import StringIO

st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="centered")

st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #000;
            color: #FFD700;
        }
        .stTextInput, .stTextArea, .stButton>button {
            background-color: #111 !important;
            color: #FFD700 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Senha
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    senha = st.text_input("Senha de acesso:", type="password")
    if senha == "botaelasil":
        st.session_state.autenticado = True
    else:
        st.stop()

st.title("A Gloriosa Enciclopédia")

# Armazenamento de temporadas
if "temporadas" not in st.session_state:
    st.session_state.temporadas = {}

st.subheader("Importar nova temporada")
nome_temporada = st.text_input("Nome da temporada")
tabela_colada = st.text_area("Cole aqui a tabela da aba 'Statistics' do Challenge Place")

# Função para limpar e formatar o texto da tabela copiada
def limpar_tabela(tabela_colada):
    # Expressão regular para separar os dados dos jogadores
    pattern = r"(\d+)\s+([A-Za-z\s\.]+)\s+([A-Za-z\s]+)\s+(\d+)"
    matches = re.findall(pattern, tabela_colada)

    # Verifica se encontrou dados e os organiza em um formato mais adequado
    if not matches:
        st.error("Tabela não pôde ser processada. Certifique-se de copiar a tabela corretamente.")
        return None

    dados = []
    for match in matches:
        # Desconstrua a linha para formar uma lista de valores
        dados.append({
            "Posição": match[0],
            "Jogador": match[1].strip(),
            "Time": match[2].strip(),
            "Gols": int(match[3]),
        })

    # Convertendo a lista de dicionários para um DataFrame
    df = pd.DataFrame(dados)
    return df

if st.button("Importar tabela"):
    df = limpar_tabela(tabela_colada)
    if df is not None:
        st.session_state.temporadas[nome_temporada] = df
        st.success(f"Temporada '{nome_temporada}' importada com sucesso!")
        st.write(df)

st.subheader("Fazer pergunta")

pergunta = st.text_input("Digite sua pergunta")
if st.button("Responder"):
    if not st.session_state.temporadas:
        st.warning("Nenhuma temporada importada ainda.")
    elif pergunta.strip() == "":
        st.warning("Digite uma pergunta.")
    else:
        resposta = responder_pergunta(pergunta, st.session_state.temporadas)
        st.markdown(resposta)
