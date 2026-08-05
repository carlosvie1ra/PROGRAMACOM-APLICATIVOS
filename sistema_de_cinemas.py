import sqlite3

conexao = sqlite3.connect('cinemas.db')
cursor = conexao.cursor()

def criar_tabelas_cinema():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cinema TEXT NOT NULL,
            shopping TEXT NOT NULL
    )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER NOT NULL,
            capacidade INTEGER NOT NULL,
            id_cinemas INTEGER NOT NULL,
            FOREIGN KEY (id_cinemas) REFERENCES cinemas(id)
        )''')
    conexao.commit()

def cadastrar_cinema():

    try:
        print("\n ---CINEMA--- ")
        nome_cinema = input("QUAL O NOME DO SEU CINEMA?: ")
        shopping = input("EM QUAL SHOPPING SE ESTABELECE LOCALIZADO?: ")

        cursor.execute("INSERT INTO cinemas (nome_cinema, shopping) VALUES (?, ?)", 
                        (nome_cinema, shopping))
        conexao.commit()
        print("\n ---cinema cadastrado: com sucesso!!!--- ")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar cinemas: {e}")

def cadastrar_salas():

    try:
        print("\n ---SALAS--- ")
        numero_sala = int(input("QUAL O NUMERO DA SUA SALA?: "))
        capacidade = int(input("QUAL A CAPACIDADE DA SALA?: "))
        id_cinemas = int(input("QUAL O ID DO CINEMA?: "))

        cursor.execute("INSERT INTO salas (numero_sala, capacidade, id_cinemas) VALUES (?, ?, ?)",
                        (numero_sala, capacidade, id_cinemas))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: ID do CINEMA inexistente!")
    except ValueError:
        print("Erro: CAPACIDAD, ID e NUMERO DA SALA do CINEMA devem ser números inteiros!")

def listar():
    print("\n --- LISTA DE SALAS ---")
    try:
        cursor.execute('SELECT * FROM salas')
        todas_salas = cursor.fetchall()
        
        if not todas_salas:
            print("Nenhuma sala cadastrada.")
            return

        for sala in todas_salas:
            print(f"ID: {sala[0]} | Sala Nº: {sala[1]} | Capacidade: {sala[2]} | ID Cinema: {sala[3]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar salas: {e}")

criar_tabelas_cinema()
cadastrar_cinema()
cadastrar_salas()
listar()

conexao.close()