import sqlite3

def cadastro_de_aluno():

    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n ---CADASTRAR NOVO ALUNO--- ")

        nome_aluno = input("DIGITE O NOME DO ALUNO: ")
        sala_aluno = input("DIGITE A SALA DO ALUNO A CADASTRAR: ")
        idade_aluno = int(input("DIGITE A IDADE(EM NUMEROS): "))
        id_aluno = int(input("INFORME O ID DO ALUNO: "))

        cursor.execute("INSERT INTO alunos (nome_aluno, sala_aluno, idade_aluno, id_aluno) VALUES (?, ?, ?, ?)", (nome_aluno, sala_aluno, idade_aluno, id_aluno))
        conexao.commit()
    
    except sqlite3.Error as e:
        print(f" Erro no banco de dados ao cadastrar aluno: {e}")
    except ValueError:
        print("ERROR: Ao cadastrar o aluno o id e a idade deve ser numeros e não letras!")

def listar_aluno():

    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n ---ALUNOS CADASTRADAS--- ")

        cursor.execute("SELECT * FROM alunos;")
        alunos = cursor.fetchall()

        print("\n --- ALUNOS ---")
        if not escolas:
            print("Nenhum aluno cadastrado no momento.")
            return
        for a in alunos:
            print(f"ID ESCOLA: {a[0]} | ALUNO: {a[1]} | SALA: {a[2]} | IDADE: {a[3]} | ID ALUNO: {a[4]}")

    except sqlite3.Error as e:
        print(f" Erro ao listar ALUNO: {e}")

def deletar_aluno():

    try:
        conexao = connect.sqlite3('banco_escola.db')
        cursor = conexao.cursor()
        print("\n ---EXCLUIR ALUNO--- ")
        id_escola = int(input("Informe o ID do aluno que deseja deletar: "))

        cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_aluno,))
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

def alterar_marca():
    
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