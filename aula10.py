valor_da_compra = float(input("digite o valor da compra: "))
prime = input("voce e cliente prime? s/n")

frete = 50.00

if valor_da_compra > 500.00 or (prime == "s" and valor_da_compra > 100.00):
    print("o seu frete e gratis!")

