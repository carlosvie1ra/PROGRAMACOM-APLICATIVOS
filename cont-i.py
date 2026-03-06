total_garrafas = int(input("Digite o número total de garrafas produzidas hoje: "))

alerta_disparado = False

if total_garrafas % 100 == 0:
    print("QUALIDADE: Retirar amostra para teste.")
    alerta_disparado = True

if total_garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")
    alerta_disparado = True

if not alerta_disparado:
    print(f"Produção em dia. Garrafa número [{total_garrafas}] processada.")
