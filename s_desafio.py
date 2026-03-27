livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
livro_desejado = "Python Pro" 

if livro_desejado in livros_disponiveis:
    livros_disponiveis.remove(livro_desejado)
    livros_emprestados.append(livro_desejado)
    print(f"Empréstimo de '{livro_desejado}' realizado com sucesso!")
else:
    print("Desculpe, este livro não está no acordo")

livro_devolvido = "Python Pro"

if livro_devolvido in livros_emprestados:
    livros_emprestados.remove(livro_devolvido)
    livros_disponiveis.append(livro_devolvido)
    print(f"Devolução de '{livro_devolvido}' concluída.")
else:
    print("Este livro não consta como emprestado.")

if len(livros_disponiveis) >= 2:
    del livros_disponiveis[0:2]

print("\n--- Relatório Final do Sistema ---")
print(f"Livros Disponíveis: {livros_disponiveis}")
print(f"Livros Emprestados: {livros_emprestados}")
