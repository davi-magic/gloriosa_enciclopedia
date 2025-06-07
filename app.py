import streamlit as st
from core.loader import carregar_temporadas
from core.engine import responder_pergunta

st.set_page_config(page_title='Gloriosa Enciclopédia', layout='wide')

st.markdown("<h1 style='text-align: center; color: gold;'>⭐ Gloriosa Enciclopédia ⭐</h1>", unsafe_allow_html=True)

senha = st.text_input("Digite a senha para acessar:", type="password")

if senha != "botaelasil":
    st.warning("Acesso restrito.")
    st.stop()

link = st.text_input("Cole o link da temporada do Challenge Place:")

if link:
    dados = carregar_temporadas(link)
    pergunta = st.text_input("Pergunte algo sobre o campeonato:")
    if pergunta:
        resposta = responder_pergunta(pergunta, dados)
        st.markdown(f"**Resposta:** {resposta}")
# Arquivo principal do Streamlit com a interface preta e dourada, importação de links e IA funcional
