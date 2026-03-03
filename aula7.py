nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
ingresso = input("voce tem ingresso? s/n ")
lista = input("voce esta na lista vip s/n ")

if idade >=18 and (ingresso == "s" or lista == "s"):
    print("seja bem vindo!")
elif idade <18 and (ingresso == "n" or lista == "n"):
    print("voce nao compre os requisitos!")