cargo = input("digite seu cargo: ")
codigo = input("digite a senha: ")
botao_de_emergencia = input("acionar o botao de emergencia (S/N)")
equipamento = input("voce esta com equipamento? (S/N) ")

if (cargo == "engenheiro" or cargo == "tecnico") and (codigo == "1235" or botao_de_emergencia == "S") and equipamento == "S":
    print("acesso liberado!")

else: 
    print("acesso negado!")