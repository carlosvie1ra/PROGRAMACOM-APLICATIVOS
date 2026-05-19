import json

# pede a mensagem ao usuário
frase = input("Digite sua mensagem: ")

# cria o dicionário
dados = {
    "mensagem": frase
}

# salva no arquivo JSON
with open("teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

print("Mensagem salva com sucesso em teste.json!")