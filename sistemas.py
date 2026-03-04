saldo_inicial = 1000.00 #variavel float

deposito = float(input("quanto voce quer depositar: "))
saque = float(input("quanto voce deseja sacar: "))
extrato_deposito = {"tipo": "deposito", "valor": deposito, "data": "04/03/2026"}
print(extrato_deposito)
extrato_saque = {"tipo": "saque", "valor": saque, "data": "04/03/2026"}
print(extrato_saque)

extrato_final = deposito - saque
print("voce ainda tem em conta: ", extrato_final)