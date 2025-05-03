import requests
import pandas as pd
from bs4 import BeautifulSoup

def carregar_dados_do_link(link):
    try:
        # Garante que o link esteja na aba de estatísticas
        if "/statistics" not in link:
            link = link.rstrip("/") + "/statistics"

        response = requests.get(link)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        if table is None:
            return None

        df = pd.read_html(str(table))[0]

        # Corrige colunas esperadas
        if "Jogador" not in df.columns:
            return None
        if "Gols" not in df.columns:
            df["Gols"] = 0
        if "Assistências" not in df.columns:
            df["Assistências"] = 0

        df["Gols"] = pd.to_numeric(df["Gols"], errors="coerce").fillna(0).astype(int)
        df["Assistências"] = pd.to_numeric(df["Assistências"], errors="coerce").fillna(0).astype(int)
        df["Participações"] = df["Gols"] + df["Assistências"]

        return df

    except Exception as e:
        print("Erro ao carregar dados:", e)
        return None
