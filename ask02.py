ataque_do_heroi = float(input("digite seu poder de ataque heroi: "))

defesa_do_vilão = float(input("digite seu poder de defesa vilão: "))

dano = ataque_do_heroi - defesa_do_vilão

if dano <= 0 :
    print("O vilão bloqueou o ataque! Dano: 0")
elif dano > 0 :
    print("Ataque crítico! Você causou dano ao vilão de: ",dano)