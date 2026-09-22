num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+ ou -): ")

match operacao:
    case "+":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
        
    case "-":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
        
    case _:
        print("Operação inválida")
