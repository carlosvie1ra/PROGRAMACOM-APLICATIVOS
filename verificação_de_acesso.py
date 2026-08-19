def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False
aaaaaaaa
assert pode_entrar(20, False) == True, "Erro: Maior de idade sozinho"
assert pode_entrar(12, True) == True, "Erro: Menor de idade acompanhado"
assert pode_entrar(25, True) == True, "Erro: Maior de idade acompanhado"

assert pode_entrar(15, False) == False, "Erro: Menor de idade sozinho"
