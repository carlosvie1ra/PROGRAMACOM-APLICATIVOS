import sqlite3

conexao = sqlite3.connect('hospital.db')
cursor = conexao.cursor()

def criar_tabela_medicos():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_hospital TEXT NOT NULL,
            cidade_hospital TEXT NOT NULL
        )''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_medico TEXT NOT NULL,
            crm INTEGER UNIQUE NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )''')
    conexao.commit()

def cadastrar_hospitais():
    try:
        print("\n ---HOSPITAL--- ")
        nome_hospital = input("INFORME O NOME DO HOSPITAL: ")
        cidade_hospital = input("INFORME A CIDADE: ")

        cursor.execute("INSERT INTO hospitais (nome_hospital, cidade_hospital) VALUES (?, ?)", 
                       (nome_hospital, cidade_hospital))
        conexao.commit()
        print("Hospital cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar hospital: {e}")

def cadastrar_medicos():
    try:
        print("\n ---MEDICO--- ")
        nome_medico = input("NOME COMPLETO: ")
        crm = int(input("INFORME O CRM: "))
        id_hospital = int(input("INFORME O ID DO HOSPITAL DE CADASTRO: "))


        cursor.execute("INSERT INTO medicos (nome_medico, crm, id_hospital) VALUES (?, ?, ?)",
                       (nome_medico, crm, id_hospital))
        conexao.commit()
        print("Médico cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: ID do hospital inexistente!")
    except ValueError:
        print("Erro: CRM e ID do Hospital devem ser números inteiros!")

criar_tabela_medicos()  
cadastrar_hospitais()   
cadastrar_medicos()     

conexao.close()