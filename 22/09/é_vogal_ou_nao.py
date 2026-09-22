letra = input("Digite uma única letra: ")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("É uma vogal")
    case _:
        print("Não é uma vogal")
