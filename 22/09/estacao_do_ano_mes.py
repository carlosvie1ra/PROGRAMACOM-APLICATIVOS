estacao = int(input("digite um mes do ano(1 a 12): "))

match estacao:
    case 12 | 1 | 2:
        print(" verão! ")

    case 3 | 4 | 5:
        print(" Outono! ")

    case 6 | 7 | 8:
        print(" inverno! ")

    case 9 | 10 | 11:
        print(" primavera! ")

    case _:
        print("mes não existente!")