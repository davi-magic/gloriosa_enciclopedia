import streamlit as st
from utils import extrair_artilheiros_assistencias as importar_tabela

st.set_page_config(page_title="A Gloriosa Enciclopédia", layout="wide")
st.title("A Gloriosa Enciclopédia - Temporadas de Futebol")

st.markdown("**Importe os dados da temporada (copie e cole o texto da tabela):**")
input_text = st.text_area("Cole aqui o conteúdo da tabela", height=400)

if st.button("Importar"):
    if not input_text.strip():
        st.warning("Nenhuma tabela foi fornecida.")
    else:
        try:
            artilheiros, assistencias = importar_tabela(input_text)
            st.success("Tabela importada com sucesso!")
            
            st.subheader("Top 10 Artilheiros")
            st.dataframe(artilheiros.head(10))
            
            st.subheader("Top 10 Assistências")
            st.dataframe(assistencias.head(10))

            pergunta = st.text_input("Faça uma pergunta (ex: Quem é o maior artilheiro?):")
            if pergunta:
                resposta = ""
                if "artilheiro" in pergunta.lower():
                    top = artilheiros.iloc[0]
                    resposta = f"O maior artilheiro é {top['Jogador']} ({top['Time']}) com {top['Gols']} gols."
                elif "assist" in pergunta.lower():
                    top = assistencias.iloc[0]
                    resposta = f"O maior assistente é {top['Jogador']} ({top['Time']}) com {top['Assistências']} assistências."
                else:
                    resposta = "Pergunta não reconhecida ainda. Tente sobre artilheiros ou assistências."
                st.markdown(f"**Resposta:** {resposta}")
        except Exception as e:
            st.error(f"Erro ao importar a tabela. Detalhes: {e}")
