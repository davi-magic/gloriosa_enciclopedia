def answer_question(data, question):
    if "artilheiro" in question.lower():
        return "O maior artilheiro é Fulano com 12 gols."
    elif "mata" in question.lower():
        return "Quem mais fez gols em mata-mata foi Ciclano com 5."
    elif "fase de grupos" in question.lower():
        return "Na fase de grupos, Beltrano lidera com 7 gols."
    else:
        return "Ainda não sei responder essa pergunta com os dados disponíveis."