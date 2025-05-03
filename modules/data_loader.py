import requests
from bs4 import BeautifulSoup

def carregar_temporadas(links):
    dados = []
    for link in links:
        try:
            r = requests.get(link)
            r.raise_for_status()
            soup = BeautifulSoup(r.content, 'html.parser')

            tabela = soup.find('table')
            if tabela:
                temporada = {}
                temporada['link'] = link
                tabela_rows = tabela.find_all('tr')

                # Pega os cabeçalhos da tabela
                headers = [header.text.strip() for header in tabela_rows[0].find_all('th')]
                
                # Pega os dados das linhas
                dados_temporada = []
                for row in tabela_rows[1:]:
                    cols = row.find_all('td')
                    dados_temporada.append([col.text.strip() for col in cols])
                
                temporada['dados'] = dados_temporada
                dados.append(temporada)
            else:
                raise ValueError("Nenhuma tabela encontrada.")
        except Exception as e:
            raise ValueError(f"Erro ao extrair dados de {link}: {e}")
    
    return dados
