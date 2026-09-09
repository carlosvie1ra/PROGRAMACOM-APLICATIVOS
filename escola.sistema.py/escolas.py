import sqlite3

def cadastro_de_escola():

    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n ---CADASTRAR NOVA ESCOLA--- ")

        nome_escola = input("DIGITE O NOME DA NOVA ESCOLA: ")
        localizacao = input("DIGITE A LOCALIZÇÃO DA ESCOLA A CADASTRAR: ")
        capacidade = int(input("DIGITE A CAPACIDADE(EM NUMEROS): "))

        cursor.execute("INSERT INTO escolas (nome_escola, localizacao, capacidade) VALUES (?, ?, ?)", (nome_escola, localizacao, capacidade))
        conexao.commit()
    
    except sqlite3.Error as e:
        print(f" Erro no banco de dados ao cadastrar escola: {e}")
    except ValueError:
        print("ERROR: Ao cadastrar escola a capacidade deve ser numeros e não letras!")

def listar_escolas():

    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n ---ESCOLAS CADASTRADAS--- ")

        cursor.execute("SELECT * FROM escolas;")
        escolas = cursor.fetchall()

        print("\n --- ESCOLAS ---")
        if not escolas:
            print("Nenhuma escola cadastrada no momento.")
            return
        for e in escolas:
            print(f"ID: {e[0]} | Escola: {e[1]} | localização: {e[2]} | capacidade: {e[3]}")

    except sqlite3.Error as e:
        print(f" Erro ao listar ESCOLA: {e}")

def deletar_escola():

    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n ---EXCLUIR ESCOLA--- ")
        id_escola = int(input("Informe o ID da escola que deseja deletar: "))

        cursor.execute("SELECT * FROM escolas WHERE id = ?", (id_escola,))
        escola = cursor.fetchone()

        if escola:
            cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))
            conexao.commit()
            print(f" Escola com ID {id_escola} deletada com sucesso!")
        else:
            print(f" Nenhuma escola foi encontrada com o ID {id_escola}.")

    except ValueError:
        print("ERRO: O ID informado deve ser um número inteiro.")
    except sqlite3.IntegrityError:
        print(" ERRO DE INTEGRIDADE: Você não pode deletar esta escola porque existem alunos/professores vinculados a ela!")
    except sqlite3.Error as e:
        print(f" Erro ao deletar escola: {e}")

def alterar_escola():
    
    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n --- ALTERAR ESCOLA ---")
        id_escola = int(input("Informe o ID da escola que deseja alterar: "))
        
        cursor.execute("SELECT id FROM escolas WHERE id = ?", (id_escola,))
        escola = cursor.fetchone()
        
        if escola:
            novo_nome = input("Digite o NOVO nome da escola: ")
            nova_localizacao = input("Digite a NOVA localização: ")
            nova_capacidade = int(input("Digite a NOVA capacidade: "))
            
            cursor.execute("UPDATE escolas SET nome_escola = ?, localizacao = ?, capacidade = ? WHERE id = ?", (novo_nome, nova_localizacao, nova_capacidade, id_marca))
            conexao.commit()
            print(f" Escola com ID {id_escola} atualizada com sucesso!")
        else:
            print(f" Nenhuma escola foi encontrada com o ID {id_escola}.")
            
    except ValueError:
        print("ERRO: O ID informado deve ser um número inteiro.")
    except sqlite3.Error as e:
        print(f" Erro ao alterar a escola: {e}")
        