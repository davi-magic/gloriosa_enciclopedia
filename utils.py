import re

def extrair_placares(texto):
    return []

def extrair_artilheiros_assistencias(texto):
    artilheiros = []
    assistencias = []

    # Extrai apenas o bloco de artilheiros
    bloco_artilheiros = re.search(r'Artilheiros(.*?)Minimizar', texto, re.DOTALL)
    if bloco_artilheiros:
        linhas = re.findall(r'([A-ZÁÉÍÓÚÂÊÎÔÛÃÕa-záéíóúâêîôûãõçÇ0-9.\' \-]+?)\s+([A-Z][a-zA-Z ]+)\s+\1\s+\2\s+(\d+)', bloco_artilheiros.group(1))
        for nome, time, gols in linhas:
            artilheiros.append({'jogador': nome.strip(), 'time': time.strip(), 'gols': int(gols)})

    # Extrai apenas o bloco de assistências
    bloco_assistencias = re.search(r'Assistências(.*?)Minimizar', texto, re.DOTALL)
    if bloco_assistencias:
        linhas = re.findall(r'([A-ZÁÉÍÓÚÂÊÎÔÛÃÕa-záéíóúâêîôûãõçÇ0-9.\' \-]+?)\s+([A-Z][a-zA-Z ]+)\s+\1\s+\2\s+(\d+)', bloco_assistencias.group(1))
        for nome, time, assist in linhas:
            assistencias.append({'jogador': nome.strip(), 'time': time.strip(), 'assistencias': int(assist)})

    return artilheiros, assistencias
