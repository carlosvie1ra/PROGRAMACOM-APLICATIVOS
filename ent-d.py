codigo = int(input("Digite o Código do Drone: "))
autorizacao = input("Possui Autorização da Torre? (s/n): ")

if codigo == 999 or autorizacao == 's':
    
    bateria = int(input("Nível de Bateria (0-100): "))
    clima = input("Clima (ensolarado/chuvoso): ")
    vento = float(input("Velocidade do Vento (km/h): "))

    if bateria < 10:
        print("POUSO AUTORIZADO: Iniciando descida. (MOTIVO: EMERGÊNCIA - BATERIA CRÍTICA)")
    
    else:
        seguro_sol = (clima == "ensolarado" and vento < 30)
        seguro_chuva = (clima == "chuvoso" and vento < 10)

        if seguro_sol or seguro_chuva:
            print("POUSO AUTORIZADO: Iniciando descida.")
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")

else:
    print("ERRO 01: Drone não identificado. Retornando à base.")
