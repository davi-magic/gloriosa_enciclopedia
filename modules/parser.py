import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract_tables_from_challenge_place(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tables = pd.read_html(str(soup))
    return tables
