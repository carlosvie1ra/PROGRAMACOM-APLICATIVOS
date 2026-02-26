nivel = float(input("informe seu nivel: "))
esferas = int(input("informe o numero de esferas coletadas: "))

if nivel >= 20 and esferas >= 50 :
    print("Habilidade Super Salto desbloqueada!")
elif nivel < 20 and esferas < 50 :
    print("Requisitos insuficientes para nova habilidade")
