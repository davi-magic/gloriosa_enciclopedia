import pandas as pd

def responder_pergunta(pergunta, dados):
    # Aqui você pode adicionar a lógica para processar as perguntas
    if "maiores artilheiros" in pergunta.lower():
        return listar_maiores_artilheiros(dados)
    elif "maiores assistentes" in pergunta.lower():
        return listar_maiores_assistentes(dados)
    elif "maiores participações em gols" in pergunta.lower():
        return listar_maiores_participacoes(dados)
    else:
        return "Pergunta não reconhecida. Tente perguntar sobre artilheiros, assistentes ou participações em gols."

def listar_maiores_artilheiros(dados, top_n=10):
    artilheiros = []
    for temporada in dados:
        for jogador in temporada['dados']:
            nome = jogador[0]
            gols = int(jogador[1])  # Assumindo que a segunda coluna tem gols
            artilheiros.append((nome, gols))

    artilheiros.sort(key=lambda x: x[1], reverse=True)
    artilheiros_top = artilheiros[:top_n]
    
    resposta = "Top 10 Maiores Artilheiros:\n"
    for i, (nome, gols) in enumerate(artilheiros_top, 1):
        resposta += f"{i}. {nome} - {gols} gols\n"
    
    return resposta

def listar_maiores_assistentes(dados, top_n=10):
    assistentes = []
    for temporada in dados:
        for jogador in temporada['dados']:
            nome = jogador[0]
            assistencias = int(jogador[2])  # Assumindo que a terceira coluna tem assistências
            assistentes.append((nome, assistencias))

    assistentes.sort(key=lambda x: x[1], reverse=True)
    assistentes_top = assistentes[:top_n]
    
    resposta = "Top 10 Maiores Assistentes:\n"
    for i, (nome, assistencias) in enumerate(assistentes_top, 1):
        resposta += f"{i}. {nome} - {assistencias} assistências\n"
    
    return resposta

def listar_maiores_participacoes(dados, top_n=10):
    participacoes = []
    for temporada in dados:
        for jogador in temporada['dados']:
            nome = jogador[0]
            gols = int(jogador[1])  # Segunda coluna: Gols
            assistencias = int(jogador[2])  # Terceira coluna: Assistências
            participacoes.append((nome, gols + assistencias))

    participacoes.sort(key=lambda x: x[1], reverse=True)
    participacoes_top = participacoes[:top_n]
    
    resposta = "Top 10 Maiores Participações em Gols:\n"
    for i, (nome, participacao) in enumerate(participacoes_top, 1):
        resposta += f"{i}. {nome} - {participacao} participações\n"
    
    return resposta
