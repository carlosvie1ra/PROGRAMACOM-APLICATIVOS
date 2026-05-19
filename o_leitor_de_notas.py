import json

# Abre e lê o arquivo JSON
with open("notas.json", "r", encoding="utf-8") as arquivo:
    notas = json.load(arquivo)

# Soma das notas
soma = notas["matemática"] + notas["portugues"]

# Exibe o resultado
print("Soma das notas:", soma)