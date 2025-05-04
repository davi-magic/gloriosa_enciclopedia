import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Função para importar as tabelas de artilheiros e assistentes
def importar_tabela(url):
    # Realizando o pedido da página
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Erro ao acessar o link. Status Code: {response.status_code}")
    
    # Parse do conteúdo da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar todas as tabelas da página
    tables = soup.find_all('table')
    
    # Caso a tabela de artilheiros e assistentes tenha classes específicas
    artilheiros_table = None
    assistentes_table = None
    
    for table in tables:
        if 'Artilheiros' in table.get_text():
            artilheiros_table = table
        if 'Assistências' in table.get_text():
            assistentes_table = table
    
    if not artilheiros_table or not assistentes_table:
        raise Exception("Tabelas de artilheiros ou assistências não encontradas.")

    # Leitura das tabelas com pandas
    artilheiros_df = pd.read_html(str(artilheiros_table))[0]
    assistentes_df = pd.read_html(str(assistentes_table))[0]
    
    # Tratamento de dados para garantir que as tabelas estejam formatadas corretamente
    artilheiros_df.columns = ['Posição', 'Jogador', 'Equipe', 'Gols']
    assistentes_df.columns = ['Posição', 'Jogador', 'Equipe', 'Assistências']
    
    return artilheiros_df, assistentes_df

# Função principal do app Streamlit
def main():
    st.title("A Gloriosa Enciclopédia - Estatísticas")
    
    # Input do link da página com as tabelas
    url = st.text_input("Digite o link da tabela:", "")
    
    if url:
        try:
            artilheiros, assistentes = importar_tabela(url)
            st.subheader("Tabela de Artilheiros")
            st.dataframe(artilheiros)  # Exibe a tabela de artilheiros
            
            st.subheader("Tabela de Assistências")
            st.dataframe(assistentes)  # Exibe a tabela de assistências
            
        except Exception as e:
            st.error(f"Erro: {e}")

if __name__ == "__main__":
    main()
