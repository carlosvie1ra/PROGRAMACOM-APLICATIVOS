def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

assert calcular_desconto(100, 10) == 90.0, "Erro no desconto de 10%"

assert calcular_desconto(50, 50) == 25.0, "Erro no desconto de 50%"

assert calcular_desconto(80, 0) == 80.0, "Erro no desconto de 0%"