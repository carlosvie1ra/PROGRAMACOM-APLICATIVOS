comprimento_da_peça = input("o comprimento da peça esta entre 10 a 12 cm (S/N): ")
peça_aprovada = input("a largura esta entre 5 a 6 cm? (S/N): ")

if comprimento_da_peça == "S" and peça_aprovada == "S":
    print("peça, aprovada!")
elif comprimento_da_peça == "N" and peça_aprovada == "N":
    print("peça, reprovada!")