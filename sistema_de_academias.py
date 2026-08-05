import sqlite3

conexao = sqlite3.connect('academias.db')
cursor = conexao.cursor()

def criar_tabela_academias():
    cursor.execute("PRAGMA foreign_keys = ON")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS academias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_unidade TEXT NOT NULL,
            bairro TEXT NOT NULL
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
        bairro = input("INFORME o BAIRRO DA ACADEMIA: ")

        cursor.execute("INSERT INTO academias (nome_unidade, bairro) VALUES (?, ?)",
                        (nome_unidade, bairro))
        conexao.commit()
        print("\n --academia: cadastrada com sucesso!!!--- ")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar academias: {e}")

def cadastrar_alunos():

    try:
        nome_aluno = input("INFORME O NOME: ")
        mensalidade = int(input("VALOR DA SUA MENSALIDADE: "))
        id_academia = int(input("ID DA ACADEMIA: "))

        cursor.execute("INSERT INTO alunos (nome_aluno, mensalidade, id_academia) VALUES (?, ?, ?)",
                        (nome_aluno, mensalidade, id_academia))
        conexao.commit()
        print("\n ---aluno: cadastrado com sucesso!!!--- ")
    except sqlite3.IntegrityError:
        print("Erro: ID da ACADEMIA inexistente!")
    except ValueError:
        print("Erro: mensalidade e ID da ACADEMIA devem ser números inteiros!")

criar_tabela_academias()
cadastrar_academia()
cadastrar_alunos()

conexao.close()