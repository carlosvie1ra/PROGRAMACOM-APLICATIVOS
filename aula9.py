nome_de_usuario = input("digite seu nome de usuario: ")
senha = int(input("digite sua senha: "))

if (nome_de_usuario == "admin" or nome_de_usuario == "root") and senha == "12345":
    print("acesso liberado!")

    