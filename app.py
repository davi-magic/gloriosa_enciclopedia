import streamlit as st
from modules.interface import mostrar_interface

st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="wide")

def main():
    st.markdown(
        "<h1 style='text-align: center; color: gold;'>A Gloriosa Enciclopédia</h1>",
        unsafe_allow_html=True
    )
    mostrar_interface()

if __name__ == "__main__":
    main()
