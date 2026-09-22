sigla = input("Digite a sigla de um estado da Região Sul (PR, SC ou RS): ")

match sigla:
    case "PR":
        print("Paraná")
        
    case "SC":
        print("Santa Catarina")
        
    case "RS":
        print("Rio Grande do Sul")
        
    case _:
        print("Estado fora da região Sul")
