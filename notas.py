media_final = float(input("informe sua media final de notas: "))
porcentagem_faltas =int(input("informe sua porcentagem de presença: "))

if media_final >= 70 and porcentagem_faltas >= 75 :
    print("Parabéns! Você foi aprovado")
elif media_final < 70 and porcentagem_faltas < 75 :
    print("Reprovado. Verifique sua nota ou frequência")