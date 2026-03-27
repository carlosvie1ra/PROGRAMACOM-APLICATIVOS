compras = []
produtos = input("digite os produtos desejados: ")

while produtos != "fim":
    compras = compras + [produtos]
    produtos = input("digite um nome de um produto (eu "fim" para finalizar a compra): ")
print("lista de produtos")
for compra in compras:
    print(f"{tem}")