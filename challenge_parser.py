import requests
import pandas as pd
from bs4 import BeautifulSoup

def carregar_dados_do_link(link):
    try:
        if "/statistics" not in link:
            link = link.rstrip("/") + "/statistics"

        response = requests.get(link)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")

        if not table:
            return None

        df = pd.read_html(str(table))[0]

        # Padronização de colunas (caso estejam diferentes)
        for col in ["Gols", "Assistências"]:
            if col not in
