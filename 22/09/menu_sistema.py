opcao = int(input("Digite uma opção de 1 a 4: "))

match opcao:
    case 1:
        print("Tela de Cadastro")
    case 2:
        print("Tela de Consulta")
    case 3:
        print("Tela de Relatórios")
    case 4:
        print("Saindo do Sistema...")
    case _:
        print("Opção incorreta")