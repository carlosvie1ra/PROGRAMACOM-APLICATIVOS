media = float(input("digite sua media escolar: "))
renda = float(input("informe sua renda familiar: "))
escola = input("sua escola e publica? s/n")

if media >= 80 and (renda < 2000 or escola == "s"):
    print("ganhou a bolsa!")
else: 
    print("voce nao possui os requisitos!")