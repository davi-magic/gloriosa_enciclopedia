import streamlit as st

def login():
    st.markdown("## A Gloriosa Enciclopédia")
    password = st.text_input("Digite a senha:", type="password")
    if password == "botaelasil":
        return True
    else:
        st.warning("Senha incorreta.")
        return False
