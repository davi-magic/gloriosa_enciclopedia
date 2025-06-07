import requests
from bs4 import BeautifulSoup

def carregar_temporadas(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')

        # Simulação simples com jogos fictícios — substituir por scraping real
        dados = {
            "jogos": [
                {"time_a": "Time A", "time_b": "Time B", "gols_a": 2, "gols_b": 1, "data": "2024-01-10", "estadio": "Arena 1"},
                {"time_a": "Time C", "time_b": "Time A", "gols_a": 0, "gols_b": 3, "data": "2024-01-15", "estadio": "Arena 2"},
            ],
            "gols": [
                {"jogador": "Jogador 1", "time": "Time A", "data": "2024-01-10", "estadio": "Arena 1"},
                {"jogador": "Jogador 2", "time": "Time A", "data": "2024-01-15", "estadio": "Arena 2"},
            ],
            "assistencias": [
                {"jogador": "Jogador 3", "para": "Jogador 1"},
            ],
            "cartoes": [
                {"jogador": "Jogador 4", "tipo": "vermelho", "partida": "Time A x Time B"},
            ]
        }
        return dados
    except Exception as e:
        return {"erro": str(e)}
# Módulo para leitura e interpretação dos dados do Challenge Place
