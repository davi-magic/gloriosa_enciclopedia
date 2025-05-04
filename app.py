import streamlit as st
from perguntas import responder_pergunta
from utils import importar_tabela

st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="wide")

st.title("A Gloriosa Enciclopédia")
st.markdown("Versão de testes - Cole a tabela do Challenge Place abaixo.")

# Entrada de texto
tabela_texto = st.text_area("Cole aqui a tabela copiada do site Challenge Place")

if "temporadas" not in st.session_state:
    st.session_state.temporadas = {}

if st.button("Importar Tabela"):
    try:
        df = importar_tabela(tabela_texto)
        st.success("Tabela importada com sucesso!")
        st.session_state.temporadas = {"Temporada Atual": df}
        st.dataframe(df)
    except Exception as e:
        st.warning("Tentando processar a tabela com outro método...")
        try:
            df = importar_tabela(tabela_texto)
            st.success("Tabela importada com sucesso!")
            st.session_state.temporadas = {"Temporada Atual": df}
            st.dataframe(df)
        except Exception as e2:
            st.error(f"Erro ao importar tabela: {e2}")

# Caixa de pergunta
pergunta = st.text_input("Faça uma pergunta sobre os dados:")

if pergunta and st.session_state.temporadas:
    resposta = responder_pergunta(pergunta, st.session_state.temporadas)
    st.write(resposta)
elif pergunta:
    st.warning("Nenhuma tabela foi importada ainda.")
