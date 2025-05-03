import requests
import pandas as pd

def carregar_dados_do_link(link):
    try:
        if not link.endswith('/csv'):
            link += '/csv'

        response = requests.get(link)
        if response.status_code != 200:
            return None

        df = pd.read_csv(pd.compat.StringIO(response.text))

        df["Gols"] = df["Gols"].fillna(0)
        df["Assistências"] = df["Assistências"].fillna(0)

        df["Participações"] = df["Gols"] + df["Assistências"]

        return df

    except Exception as e:
        print("Erro ao carregar dados:", e)
        return None
