print("--- MENU DE BEBIDAS ---")
print("1 - Café")
print("2 - Chá")
print("3 - Suco")
print("-----------------------")

opcao = int(input("Escolha o número da sua bebida: "))

match opcao:
    case 1:
        print("Você escolheu Café")
        
    case 2:
        print("Você escolheu Chá")
        
    case 3:
        print("Você escolheu Suco")
        
    case _:
        print("Opção inexistente")
