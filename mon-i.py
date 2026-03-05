temperatura = float(input("Digite a temperatura atual: "))

if temperatura <= 30:
    print("Clima estável")
else:
    print("Alerta de Calor!")
    umidade = float(input("Digite a umidade atual (%): "))
    
    if umidade < 40:
        print("Ação: Ligar Irrigação!")
    else:
        print("Ação: Ligar apenas ventiladores")
