def responder_pergunta(pergunta, dados):
    pergunta = pergunta.lower()

    if "quem fez gol" in pergunta:
        return ", ".join(set(g['jogador'] for g in dados["gols"]))

    if "assistência" in pergunta:
        return ", ".join(f"{a['jogador']} → {a['para']}" for a in dados["assistencias"])

    if "cartão" in pergunta:
        return ", ".join(f"{c['jogador']} ({c['tipo']})" for c in dados["cartoes"])

    if "estádio" in pergunta or "arena" in pergunta:
        return ", ".join(set(j['estadio'] for j in dados["jogos"]))

    return "Ainda não sei responder isso com precisão, mas estou aprendendo!"
# Módulo com lógica para responder perguntas complexas
