import sqlite3

conexao = sqlite3.connect('banco_escola.db')
cursor = conexao.cursor()

def criar_tabelas_escola():
    
    try:
        cursor.execute = ("PRAGMA foreign_keys = ON")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_escola TEXT NOT NULL,
                localização TEXT NOT NULL,
                capacidade INTEGER NOT NULL
        )''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno TEXT NOT NULL,
                idade_aluno TEXT NOT NULL,
                sala_aluno TEXT NOT NULL,
                id_aluno INTEGER NOT NULL,
                FOREIGN KEY (id_aluno) REFERENCES escolas(id)
            )''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_professor TEXT NOT NULL.
                idade_professor TEXT NOT NULL,
                materia TEXT NOT NULL,
                sala TEXT NOT NULL,
                id_professor INTEGER NOT NULL,
                FOREIGN KEY (id_professor) REFERENCES escolas(id)
            )''')
            
        print("Banco de dados inicializado com sucesso!")
            
        conexao.commit()

    except sqlite3.Error as e:
        print(f" Erro ao inicializar o banco de dados: {e}")
        return None

criar_tabelas_escola()