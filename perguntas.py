def responder_pergunta(pergunta, temporadas):
    import pandas as pd
    import re

    todas = pd.concat(temporadas.values(), ignore_index=True)
    pergunta_lower = pergunta.lower()

    def top(df, coluna):
        return df.sort_values(by=coluna, ascending=False)[["Jogador", coluna]].head(10)

    if "gols" in pergunta_lower and "assistência" in pergunta_lower:
        df = todas.copy()
        if "da" in pergunta_lower or "do" in pergunta_lower:
            for nome, temp in temporadas.items():
                if nome.lower() in pergunta_lower:
                    df = temp.copy()
                    break
        df["Participações"] = df["Gols"] + df["Assistências"]
        tabela = top(df, "Participações")
        return "**Top 10 participações em gols:**\n\n" + tabela.to_markdown(index=False)

    if "artilheiro" in pergunta_lower or "mais gols" in pergunta_lower:
        df = todas.copy()
        if "da" in pergunta_lower or "do" in pergunta_lower:
            for nome, temp in temporadas.items():
                if nome.lower() in pergunta_lower:
                    df = temp.copy()
                    break
        tabela = top(df, "Gols")
        return "**Top 10 artilheiros:**\n\n" + tabela.to_markdown(index=False)

    if "assistência" in pergunta_lower:
        df = todas.copy()
        if "da" in pergunta_lower or "do" in pergunta_lower:
            for nome, temp in temporadas.items():
                if nome.lower() in pergunta_lower:
                    df = temp.copy()
                    break
        tabela = top(df, "Assistências")
        return "**Top 10 assistentes:**\n\n" + tabela.to_markdown(index=False)

    return "Não entendi a pergunta. Tente perguntar sobre artilheiros, assistências ou participações em gols."
