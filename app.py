import streamlit as st
from modules.login import login
from modules.parser import parse_data
from modules.qa import answer_question
import json

st.set_page_config(page_title="Gloriosa Enciclopédia", layout="centered")

if login():
    st.title("A Gloriosa Enciclopédia")
    st.markdown("**Versão de testes com campeonato embutido**")

    with open("data/campeonato_exemplo.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    question = st.text_input("Faça sua pergunta:")
    if question:
        try:
            answer = answer_question(data, question)
            st.write(answer)
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")