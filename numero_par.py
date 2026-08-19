def eh_par(numero):
    return numero % 2 == 0

assert eh_par(4) == True, "(4) deve ser definido como numero par"

assert eh_par(3) == False, "Error: (3) não deve ser definido como numero par"

assert eh_par(0) == True, "(0) deve ser definido como um numero par"

assert eh_par(-3) == False, "Error: (-3) nâo deve ser definido como um numero par"
assert eh_par(-2) == True, "(-2) deve ser definido como numero par"

print("Erros tratados com sucesso")