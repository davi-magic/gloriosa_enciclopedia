import requests
import pandas as pd
from io import StringIO

def carregar_dados_do_link(link):
    try:
        # Corrige o link para apontar para o CSV, se necessário
        if "/statistics" in link and not link.endswith("/csv"):
            link = link.rstrip("/") + "/csv"
        elif not link.endswith("/csv"):
            link = link.rstrip("/") + "/statistics/csv"

        response = requests.get(link)
        if response.status_code != 200:
            return None

        df = pd.read_csv(StringIO(response.text))

        df["Gols"] = df["Gols"].fillna(0)
        df["Assistências"] = df["Assistências"].fillna(0)
        df["Participações"] = df["Gols"] + df["Assistências"]

        return df

    except Exception as e:
        print("Erro ao carregar dados:", e)
        return None
