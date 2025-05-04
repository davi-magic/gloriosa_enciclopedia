import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def importar_tabela(url):
    try:
        # Realiza a requisição HTTP para obter o conteúdo da página
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Analisa o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra todas as tabelas na página
        tables = soup.find_all('table')

        if not tables:
            st.error("Nenhuma tabela encontrada na página.")
            return None

        # Para este exemplo, assumimos que a primeira tabela é a de artilheiros
        # e a segunda tabela é a de assistentes. Isso pode variar dependendo da estrutura da página.
        artilheiros_df = pd.read_html(str(tables[0]))[0]
        assistentes_df = pd.read_html(str(tables[1]))[0] if len(tables) > 1 else None

        return artilheiros_df, assistentes_df

    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a URL: {e}")
        return None, None
    except ValueError as e:
        st.error(f"Erro ao processar as tabelas: {e}")
        return None, None

def main():
    st.title("Importador de Estatísticas do Challenge Place")

    url = st.text_input("Insira o link da página de estatísticas do Challenge Place:")

    if url:
        artilheiros_df, assistentes_df = importar_tabela(url)

        if artilheiros_df is not None:
            st.subheader("Tabela de Artilheiros")
            st.dataframe(artilheiros_df)

        if assistentes_df is not None:
            st.subheader("Tabela de Assistentes")
            st.dataframe(assistentes_df)

if __name__ == "__main__":
    main()
