nome = input("nome de usuario: ")
codigo = int(input("informe o code de segurança: "))

if codigo == "999":
    print("bem vindo ao nosso site!")
else: 
    print("codigo invalido! informe o codigo novamente", codigo)