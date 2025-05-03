import pandas as pd

def responder_pergunta(pergunta, df):
    pergunta = pergunta.lower()
    n = 10  # padrão top 10

    # detecta se o usuário pediu outro número
    for palavra in pergunta.split():
        if palavra.isdigit():
            n = int(palavra)

    if "artilheiro" in pergunta or "gols" in pergunta:
        ranking = df.groupby("Jogador")["Gols"].sum().sort_values(ascending=False).head(n)
        titulo = f"Top {n} artilheiros"
    elif "assistência" in pergunta:
        ranking = df.groupby("Jogador")["Assistências"].sum().sort_values(ascending=False).head(n)
        titulo = f"Top {n} assistências"
    elif "participação" in pergunta:
        ranking = df.groupby("Jogador")["Participações"].sum().sort_values(ascending=False).head(n)
        titulo = f"Top {n} participações em gols"
    else:
        return "Não entendi a pergunta. Tente algo como 'Quem é o artilheiro da história?'."

    resultado = f"### {titulo}\n"
    resultado += ranking.to_frame().reset_index().to_markdown(index=False)
    return resultado
