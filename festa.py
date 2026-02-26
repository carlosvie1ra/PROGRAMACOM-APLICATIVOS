idade = int(input("informe sua idade: "))
saldo = float(input("informe seu saldo: "))

if idade >= 18 and saldo >= 50 :
    print("Acesso autorizado! Bem-vindo ao evento")
elif idade < 18 and saldo < 50 :
    print("Infelizmente você não cumpre os requisitos de entrada")

