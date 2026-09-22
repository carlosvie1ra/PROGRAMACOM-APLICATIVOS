conceito = input("Digite o seu conceito (A, B, C, D ou F): ").upper()

match conceito:
    case "A" | "B":
        print("Excelente desempenho")
        
    case "C" | "D":
        print("Desempenho mediano")
        
    case "F":
        print("Reprovado")
        
    case _:
        print("Conceito inválido")
