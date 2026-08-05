import sqlite3

conexao = sqlite3.connect('academias.db')
cursor = conexao.cursor()

def criar_tabela_academias():
    cursor.execute("PRAGMA foreign_keys = ON")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS academias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_unidade TEXT NOT NULL,
            idade INTEGER NOT NULL
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_aluno TEXT NOT NULL,
        mensalidade INTEGER NOT NULL,
        id_academia INTEGER NOT NULL,
        FOREIGN KEY (id_academia) REFERENCES academias(id)
    )''')
conexao.commit()

def cadastrar_academia():

    try:
        nome_unidade = input("NOME DA UNIDADE: ")
        idade = int(input("INFORME A IDADE: "))

        cursor.execute("INSER INTO academias (nome_unidade, idade) VALUES (?, ?)",
                        (nome_unidade, idade))
        conexao.commit()
        print("\n ---cinema academia: com sucesso!!!--- ")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar academias: {e}")

def cadastrar_alunos():

    try:
        nome_aluno = input("INFORME O NOME: ")

        