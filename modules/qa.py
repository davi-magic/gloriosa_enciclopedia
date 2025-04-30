import pandas as pd

def answer_question(df, question):
    # Exemplo de resposta simples
    if "artilheiro" in question.lower():
        artilheiro = df.groupby("Jogador")["Gols"].sum().idxmax()
        return f"O maior artilheiro é {artilheiro}."
    else:
        return "Ainda não sei responder essa pergunta."
# Módulo de perguntas e respostas
