from modules.data_loader import carregar_dados
from modules.query_engine import responder_pergunta
import streamlit as st

def mostrar_interface():
    st.title("A Gloriosa Enciclopédia")
    st.markdown("Importe uma temporada do Challenge Place e faça suas perguntas.")

    uploaded_file = st.file_uploader("Importe o CSV da temporada", type="csv")

    if uploaded_file is not None:
        df = carregar_dados(uploaded_file)
        st.success("Temporada carregada com sucesso!")

        pergunta = st.text_input("Pergunte algo (ex: quem é o artilheiro?)")
        if pergunta:
            resposta = responder_pergunta(df, pergunta)
            st.markdown("**Resposta:**")
            st.write(resposta)
