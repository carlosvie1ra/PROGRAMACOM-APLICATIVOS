valor_total = float(input("Digite o valor total da compra: R$ "))

cupom = input("Digite o nome do cupom: ")

if cupom == "DEV10":
    desconto = valor_total * 0.10
    novo_preco = valor_total - desconto
    print("Cupom aplicado! Novo preço com 10% de desconto: ",novo_preco)
else:
    print("Cupom inválido. Valor original: ",valor_total)