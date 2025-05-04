import pandas as pd
import re

def extrair_artilheiros_assistencias(texto):
    linhas = texto.splitlines()
    artilheiros = []
    assistencias = []

    modo = None
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        if "Artilheiros" in linha:
            modo = "gols"
            continue
        if "Assistências" in linha:
            modo = "assists"
            continue
        if modo in ["gols", "assists"]:
            partes = re.split(r"\s{2,}", linha)
            if len(partes) < 3:
                partes = re.findall(r"(.*?)\s([^\d\s]+(?:\s[^\d\s]+)*)\s(\d+)", linha)
                if partes:
                    partes = partes[0]
            if isinstance(partes, (list, tuple)) and len(partes) >= 3:
                jogador = partes[0].strip()
                time = partes[1].strip()
                valor = int(partes[2])
                if modo == "gols":
                    artilheiros.append({"Jogador": jogador, "Time": time, "Gols": valor})
                else:
                    assistencias.append({"Jogador": jogador, "Time": time, "Assistências": valor})
    if not artilheiros and not assistencias:
        raise ValueError("Não foi possível identificar linhas de tabela válidas.")
    
    df_gols = pd.DataFrame(artilheiros).sort_values("Gols", ascending=False).reset_index(drop=True)
    df_assists = pd.DataFrame(assistencias).sort_values("Assistências", ascending=False).reset_index(drop=True)
    
    return df_gols, df_assists
