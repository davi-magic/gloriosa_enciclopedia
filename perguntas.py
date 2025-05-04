def responder_pergunta(pergunta, temporadas):
    df = list(temporadas.values())[0]

    if "artilheiro" in pergunta.lower():
        if "gols" in df.columns:
            artilheiros = df[["nome", "gols"]].sort_values(by="gols", ascending=False).head(10)
            return artilheiros.reset_index(drop=True)
        else:
            return "Não encontrei a coluna de gols na tabela."

    elif "assistência" in pergunta.lower():
        colunas_possiveis = [col for col in df.columns if "assist" in col.lower()]
        if colunas_possiveis:
            col = colunas_possiveis[0]
            assistentes = df[["nome", col]].sort_values(by=col, ascending=False).head(10)
            return assistentes.reset_index(drop=True)
        else:
            return "Não encontrei a coluna de assistências."

    elif "participação" in pergunta.lower() or "gols + assistências" in pergunta.lower():
        col_gols = [col for col in df.columns if "gol" in col.lower()]
        col_assist = [col for col in df.columns if "assist" in col.lower()]
        if col_gols and col_assist:
            df["participações"] = df[col_gols[0]] + df[col_assist[0]]
            top_participacoes = df[["nome", "participações"]].sort_values(by="participações", ascending=False).head(10)
            return top_participacoes.reset_index(drop=True)
        else:
            return "Faltam colunas de gols ou assistências para calcular participações."

    else:
        return "Desculpe, ainda não sei responder esse tipo de pergunta."
