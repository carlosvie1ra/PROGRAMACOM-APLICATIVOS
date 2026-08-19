def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

assert situacao_aluno(6) == "aprovado", "Error: (6) Aluno aprovado na media"

assert situacao_aluno(7) == "aprovado", "Error: (7) aluno aprovado acima da media"

assert situacao_aluno(5) == "recuperação", "Error: (5) aluno reprovado abaixo da media"
assert situacao_aluno(4) == "recuperação", "Error: (4) aluno na recuperação"

assert situacao_aluno(3) == "Reprovado", "Error: (3) aluno reprovado"

assert situacao_aluno9(-6) == "reprovado", "Error: (-6) aluno reprovado"