import streamlit as st
from utils import extrair_dados_challenge_place

st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="wide")
st.title("📊 A Gloriosa Enciclopédia - Temporadas do Challenge Place")

url = st.text_input("Cole o link da aba 'Estatísticas' do Challenge Place:")

if url:
    try:
        df = extrair_dados_challenge_place(url)
        st.success("Dados carregados com sucesso!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erro ao extrair dados: {e}")