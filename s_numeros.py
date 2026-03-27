lista = [1, 5, 8, 12, 15, 22, 7, 9, 30, 4]
pares = []
impares = []

for nume in lista:
    if nume  % 2 == 0:
        psres.append(nume)
    else:
        impar.append(nume)
print(f"IMPAR: {impar}")
print(f"PAR: {pares}")
