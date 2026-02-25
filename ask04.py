temperatura = float(input("Digite a temperatura do servidor: "))

if temperatura >= 80:
    print("PERIGO! Desligando servidor por superaquecimento!")
elif temperatura >= 50:
    print("Alerta: Ventoinhas ligadas no máximo!")
else:
    print("Temperatura estável. Sistema operando normalmente.")