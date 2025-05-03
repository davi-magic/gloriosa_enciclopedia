def responder_pergunta(df, pergunta):
    pergunta = pergunta.lower()

    if "artilheiro" in pergunta:
        return df.groupby("Jogador")["Gols"].sum().sort_values(ascending=False).head(10)

    elif "assistência" in pergunta:
        return df.groupby("Jogador")["Assistências"].sum().sort_values(ascending=False).head(10)

    elif "participação" in pergunta or "participações" in pergunta:
        df["Participações"] = df["Gols"] + df["Assistências"]
        return df.groupby("Jogador")["Participações"].sum().sort_values(ascending=False).head(10)

    else:
        return "Desculpe, ainda não sei responder essa pergunta."
