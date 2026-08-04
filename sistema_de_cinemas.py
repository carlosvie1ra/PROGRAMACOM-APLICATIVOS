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

criar_tabelas_cinema