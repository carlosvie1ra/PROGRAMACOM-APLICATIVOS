import sqlite3

def criar_tabelas_texteis():
    conexao = sqlite3.connect('fabrica.db')
    cursor = conexao.cursor()
    
    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute("PRAGMA foreign_keys = ON")
       
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS marcas_moda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                grife_nome TEXT NOT NULL,
                registro_patente TEXT NOT NULL
        )''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fabricas_texteis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                distrito_industrial TEXT NOT NULL,
                id_marca INTEGER NOT NULL,
                FOREIGN KEY (id_marca) REFERENCES marcas_moda(id)
            )''')
        conexao.commit()
        print(" Banco de dados inicializado com sucesso!")
        return conexao
    
    except sqlite3.Error as e:
        print(f" Erro ao inicializar o banco de dados: {e}")
        return None

def cadastrar_marcas(conexao):

    try:
        cursor = conexao.cursor()
        print("\n ---CADASTRO DE NOVA MARCA--- ")
        grife_nome = input("QUAL SUA MARCA, QUE DESEJA CADASTRAR?: ")
        registro_patente = input("CRIE O SEU REGISTRO DA PATENTE: ")
        
        cursor.execute("INSERT INTO marcas_moda (grife_nome, registro_patente) VALUES (?, ?)", (grife_nome, registro_patente))
        conexao.commit()
        print(f"Marca '{grife_nome}' Cadastrada com sucesso, seu registro de patente é {registro_patente}")
    except sqlite3.Error as e:
        print(f" Erro no banco de dados ao cadastrar marca: {e}")
    except ValueError:
        print("ERROR: Ao cadastrar a marca o nome deve ser letras e não numeros!")

def cadastrar_fabricas(conexao):

    try:
        cursor = conexao.cursor()
        print("\n ---CADASTRO DE NOVA FABRICA--- ")
        distrito_industrial = input("INFORME O DISTRITO: ")
        id_marca = int(input("QUAL O ID DA MARCA QUE DESEJA VINCULAR A FABRICA?: "))
        
        cursor.execute("INSERT INTO fabricas_texteis (distrito_industrial, id_marca) VALUES (?, ?)", (distrito_industrial, id_marca))
        conexao.commit()
        print(f"Fabrica '{distrito_industrial}' Vinculada com sucesso a marca com id {id_marca}")

    except ValueError:
        print("ERRO DE DIGITAÇÃO: O id deve ter apenas numeros inteiros, e nenhuma letra virgula ou pontuacão")
    except sqlite3.Error as e:
        print(f"erro no banco de dados: {e}")
        print(" Dica: Verifique se o ID da marca informado realmente existe na tabela de marcas_moda.")

def listar_marcas(conexao):

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, grife_nome, registro_patente FROM marcas_moda;")
        marcas_moda = cursor.fetchall()
        
        print("\n--- Lista de marcas Cadastradas ---")
        if not marcas_moda:
            print("Nenhuma marca cadastrada no momento.")
            return
        
        for m in marcas_moda:
            print(f"ID: {m[0]} | Marca: {m[1]} | Registro de patente: {m[2]}")
            
    except sqlite3.Error as e:
        print(f" Erro ao listar marcas: {e}")

def listar_fabricas(conexao):

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, distrito_industrial, id_marca FROM fabricas_texteis;")
        fabricas_texteis = cursor.fetchall()

        print("\n--- lista de fabricas vinculadas/cadastradas ---")
        if not fabricas_texteis:
            print("nenhuma fabrica cadastrada no momento.")
            return

        for f in fabricas_texteis:
            print(f"ID: {f[0]} | distrito: {f[1]} | id da marca vinculada: {f[2]}")

    except sqlite3.Error as e:
        print(f" Erro ao listar fabricas: {e}")

def deletar_marca(conexao):
    try:
        cursor = conexao.cursor()
        print("\n --- DELETAR MARCA ---")
        id_marca = int(input("Informe o ID da marca que deseja deletar: "))
        
        cursor.execute("SELECT id FROM marcas_moda WHERE id = ?", (id_marca,))
        marca = cursor.fetchone()
        
        if marca:
            cursor.execute("DELETE FROM marcas_moda WHERE id = ?", (id_marca,))
            conexao.commit()
            print(f" Marca com ID {id_marca} deletada com sucesso!")
        else:
            print(f" Nenhuma marca foi encontrada com o ID {id_marca}.")
            
    except ValueError:
        print("ERRO: O ID informado deve ser um número inteiro.")
    except sqlite3.IntegrityError:
        print(" ERRO DE INTEGRIDADE: Você não pode deletar esta marca porque existem fábricas vinculadas a ela!")
    except sqlite3.Error as e:
        print(f" Erro ao deletar marca: {e}")

def deletar_fabrica(conexao):
    try:
        cursor = conexao.cursor()
        print("\n --- DELETAR FÁBRICA ---")
        id_fabrica = int(input("Informe o ID da fábrica que deseja deletar: "))
        
        cursor.execute("SELECT id FROM fabricas_texteis WHERE id = ?", (id_fabrica,))
        fabrica = cursor.fetchone()
        
        if fabrica:
            cursor.execute("DELETE FROM fabricas_texteis WHERE id = ?", (id_fabrica,))
            conexao.commit()
            print(f" Fábrica com ID {id_fabrica} deletada com sucesso!")
        else:
            print(f" Nenhuma fábrica foi encontrada com o ID {id_fabrica}.")
            
    except ValueError:
        print("ERRO: O ID informado deve ser um número inteiro.")
    except sqlite3.Error as e:
        print(f" Erro ao deletar fábrica: {e}")

def alterar_marca(conexao):
    try:
        cursor = conexao.cursor()
        print("\n --- ALTERAR MARCA ---")
        id_marca = int(input("Informe o ID da marca que deseja alterar: "))
        
        cursor.execute("SELECT id FROM marcas_moda WHERE id = ?", (id_marca,))
        marca = cursor.fetchone()
        
        if marca:
            novo_nome = input("Digite o NOVO nome da marca: ")
            novo_registro = input("Digite o NOVO registro de patente: ")
            
            cursor.execute("UPDATE marcas_moda SET grife_nome = ?, registro_patente = ? WHERE id = ?", (novo_nome, novo_registro, id_marca))
            conexao.commit()
            print(f" Marca com ID {id_marca} atualizada com sucesso!")
        else:
            print(f" Nenhuma marca foi encontrada com o ID {id_marca}.")
            
    except ValueError:
        print("ERRO: O ID informado deve ser um número inteiro.")
    except sqlite3.Error as e:
        print(f" Erro ao alterar marca: {e}")

def alterar_fabrica(conexao):
    try:
        cursor = conexao.cursor()
        print("\n --- ALTERAR FÁBRICA ---")
        id_fabrica = int(input("Informe o ID da fábrica que deseja alterar: "))
        
        cursor.execute("SELECT id FROM fabricas_texteis WHERE id = ?", (id_fabrica,))
        fabrica = cursor.fetchone()
        
        if fabrica:
            novo_distrito = input("Digite o NOVO distrito industrial: ")
            novo_id_marca = int(input("Digite o NOVO ID da marca vinculada: "))
            
            cursor.execute("UPDATE fabricas_texteis SET distrito_industrial = ?, id_marca = ? WHERE id = ?", (novo_distrito, novo_id_marca, id_fabrica))
            conexao.commit()
            print(f" Fábrica com ID {id_fabrica} atualizada com sucesso!")
        else:
            print(f" Nenhuma fábrica foi encontrada com o ID {id_fabrica}.")
            
    except ValueError:
        print("ERRO: Os IDs informados devem ser números inteiros.")
    except sqlite3.Error as e:
        print(f" Erro ao alterar fábrica: {e}")
        print(" Dica: Verifique se o novo ID da marca realmente existe na tabela de marcas_moda.")

def menu():
    conexao = criar_tabelas_texteis()
    if not conexao:
        return
    
    try:
        while True:
            print("\n-------------MENU DO SITE TEXTIL-------------")
            print("1. Cadastrar marca")
            print("2. Listar marcas")
            print("3. Listar fabricas")
            print("4. Cadastrar fabrica")
            print("5. Deletar marca")
            print("6. Deletar fabrica")
            print("7. Alterar marca")
            print("8. Alterar fabrica")
            print("9. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                cadastrar_marcas(conexao)
            elif opcao == "2":
                listar_marcas(conexao)
            elif opcao == "3":
                listar_fabricas(conexao)
            elif opcao == "4":
                cadastrar_fabricas(conexao)
            elif opcao == "5":
                listar_marcas(conexao)
                deletar_marca(conexao)
            elif opcao == "6":
                listar_fabricas(conexao)
                deletar_fabrica(conexao)
            elif opcao == "7":
                listar_marcas(conexao)
                alterar_marca(conexao)
            elif opcao == "8":
                listar_fabricas(conexao) 
                alterar_fabrica(conexao)
            elif opcao == "9":
                print("Encerrando o sistema... Até logo!")
                break
            else:
                print(" Opção inválida! Escolha um número entre 1 e 9.")
    finally:
        conexao.close()

if __name__ == "__main__":
    menu()