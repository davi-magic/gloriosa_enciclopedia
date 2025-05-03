import streamlit as st
from challenge_parser import carregar_dados_do_link
from perguntas import responder_pergunta

st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="wide")

# Estilo preto e dourado
st.markdown("""
    <style>
    body { background-color: #000; color: #FFD700; }
    .stApp { background-color: #000; }
    </style>
""", unsafe_allow_html=True)

# Proteção por senha
senha = st.text_input("Digite a senha para acessar:", type="password")
if senha != "botaelasil":
    st.warning("Acesso negado.")
    st.stop()

st.title("A Gloriosa Enciclopédia")

link = st.text_input("Cole o link do campeonato do Challenge Place aqui:")

if link:
    with st.spinner("Carregando dados do campeonato..."):
        dados = carregar_dados_do_link(link)

    if dados is None:
        st.error("Não foi possível carregar os dados. Verifique o link.")
    else:
        st.success("Dados carregados com sucesso! Pergunte o que quiser.")
        pergunta = st.text_input("Faça uma pergunta (ex: quem é o artilheiro da história?)")
        if pergunta:
            resposta = responder_pergunta(pergunta, dados)
            st.markdown(resposta, unsafe_allow_html=True)
