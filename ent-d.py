print("INDENTIFIQUISE!")

codigo = int(input("digite o codigo: "))
autorizacao = input("voce possui a autorizção? (S/N): ")

if codigo == "999" and autorizacao == "S":
    print("acesso permitido!")

else:
    ("ERRO 01:  Drone não identificado. Retornando à base")

print("BATERIA: 0 A 100")

nivel_bateria = input("qual o nivel da bateria: ")

print("ensolarado/chuvoso")

clima = input("informe o jeito do clima: ")
velocidade_do_vento = float(input("informe a velocidade do vento"))


if nivel_bateria <= "10":
    print("pouso de emergencia autorizado, pouca bateria")

elif (nivel_bateria > "10" and clima == "ensolarado" and velocidade_do_vento <= 30) or clima == "chuvoso" and velocidade_do_vento < 10.0:
        print("pouso autorizado!")

else:
     print("pouso negado condições metereologicas perigosas!")
