import streamlit as st
import pandas as pd
from perguntas import responder_pergunta
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

if st.button("Importar tabela"):
    try:
        # Processando a tabela colada
        tabela_io = StringIO(tabela_colada)
        
        # Tentando detectar automaticamente o separador (tab, vírgula, ou outro)
        try:
            df = pd.read_csv(tabela_io, sep=None, engine='python')
        except Exception as e:
            st.error(f"Erro ao tentar importar a tabela. Detalhes: {e}")
            st.warning("Tentando processar a tabela com outro método...")
            
            # Tentando com um delimitador padrão (tabulação ou múltiplos espaços)
            tabela_io.seek(0)
            df = pd.read_csv(tabela_io, sep=r'\s+', engine='python')
        
        if "Jogador" not in df.columns:
            st.error("Tabela inválida. Certifique-se de copiar a tabela corretamente.")
        else:
            # Convertendo as colunas de Gols e Assistências para numérico
            df["Gols"] = pd.to_numeric(df.get("Gols", 0), errors="coerce").fillna(0).astype(int)
            df["Assistências"] = pd.to_numeric(df.get("Assistências", 0), errors="coerce").fillna(0).astype(int)
            df["Participações"] = df["Gols"] + df["Assistências"]
            
            # Adicionando a temporada
            st.session_state.temporadas[nome_temporada] = df
            st.success(f"Temporada '{nome_temporada}' importada com sucesso!")
    
    except Exception as e:
        st.error(f"Erro ao importar tabela: {e}")

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
