pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
concluidos = []

print("Estado inicial:")
print(f"Pendentes: {pendentes}")
print(f"Concluídos: {concluidos}")
print()

arquivo = pendentes.pop(0)  
concluidos.append(arquivo)

print("Após transferência:")
print(f"Pendentes: {pendentes}")
print(f"Concluídos: {concluidos}")