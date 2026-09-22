codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1 | 2:
        print("Alimentos Perecíveis")
    case 3 | 4:
        print("Bebidas")
    case 5:
        print("Produtos de Limpeza")
    case _:
        print("Código não cadastrado")
