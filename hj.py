import sqlite3

# 1. Conecta ao banco de dados (se o arquivo escola.db não existir, ele será criado)
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

# 2. Cria a tabela de alunos
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    data_nascimento TEXT,
    turma TEXT
)
''')

# 3. Função para cadastrar alunos com segurança (evita SQL Injection)
def cadastrar_aluno():
    print("\n ==== REGISTRAR ALUNO ====")

    nome = input("Qual o nome completo do aluno? (obrigatório): ")
    email = input("Qual o email do aluno? (obrigatório): ")
    data_nasc = input("Qual a data de nascimento do aluno? (obrigatório): ")
    turma = input("Qual a turma do aluno? (opcional): ")

    try:
        cursor.execute('''
        INSERT INTO alunos (nome, email, data_nascimento, turma)
        VALUES (?, ?, ?, ?)
        ''', (nome, email, data_nasc, turma))
        
        conexao.commit()  # Salva as alterações no arquivo
        print(f"Aluno(a) {nome} cadastrado(a) com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: O email '{email}' já está cadastrado.")

# Chama a função para cadastrar um aluno
cadastrar_aluno()

# Fecha a conexão com o banco de dados
conexao.close()