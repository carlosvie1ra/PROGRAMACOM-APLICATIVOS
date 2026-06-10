import sqlite3

print("--- Sistema de Cadastro de Alunos ---")
nome = input("Nome Completo: ")
telefone = input("Telefone: ")
turma = input("Turma: ")
idade = input("Idade: ")
cpf = input("CPF: ")


conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

comando_insert = f"INSERT INTO alunos (nome, telefone, turma, idade, cpf) VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}')"

cursor.execute(comando_insert)
conexao.commit()
conexao.close()

print(f"\nCadastro de {nome} realizado com sucesso!")
