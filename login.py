import streamlit as st

def login():
    st.markdown("## Acesso protegido")
    senha = st.text_input("Digite a senha:", type="password")
    if senha == "botaelasil":
        return True
    elif senha:
        st.error("Senha incorreta.")
        return False
    return False