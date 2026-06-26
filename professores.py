import sqlite3 #importa o banco de dados

conexao = sqlite3.connect('escola_demonstracao.db') #conecta o banco de dados
cursor = conexao.cursor() #conecta o cursor ao banco

cursor.execute('''CREATE TABLE IF NOT EXISTS professores( 
id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
nome_professor TEXT NOT NULL,
idade_professor INTEGER NOT NULL,
materia_professor TEXT NOT NULL,
salario_professor REAL NOT NULL,
cpf_professor TEXT NOT NULL,
nome_colegio TEXT NO NULL,
endereco_professor TEXT,
telefone_professor TEXT NOT NULL)''') #coloca as informaçôes necessarias dentro do bando de dados

def registrar_professores():
    try:
        print("\n ==== REGISTRAR PROFESSORES ====")
        nome = input("Qual o nome completo do professor? (obrigatório): ")
        telefone = input("Qual o telefone do professor? (obrigatório): ")
        materia = input("Qual a matéria do professor? (opcional): ")
        idade = int(input("Qual a idade do professor?(obrigatório): "))
        cpf = input("qual o CPF do professor? (obrigatório): ")
        salario = input("qual o salário atual do professor? (opcional): ")
        nome_colegio = input("qual o nome do colégio? (obrigatório): ")
        endereco = input("qual seu endereço? (obrigatorio): ")

        comando_inserir = f'''INSERT INTO professores(nome_professor, idade_professor, materia_professor, salario_professor, cpf_professor, nome_colegio, endereco_professor, telefone_professor)
        values ('{nome}', {idade}, '{materia}', {salario}, '{cpf}', '{nome_colegio}', '{endereco}', '{telefone}')''' #pega oque eu pedi nos inputs e insere nas iformações(topicos)

        cursor.execute(comando_inserir) #insere as informações pedidas no db
        print("professor registrado com sucesso!")
        conexao.commit() #salva as informações

    except ValueError:
        print("erro de valor...")

    except NameError:
        print("erro de variavel...")
        print("buscando variavel...")
        print("variavel não encontrada!")

    except TypeError:
        print("objeto de tipo inadequado!")

    except IndexError:
        print("você tenta acessar um índice que não existe?")

    except KeyboardInterrupt:
        print("operaçãp terminada, voltando ao menu...")

def ver_professores():
    try:
        cursor.execute("SELECT * FROM professores")
        professores = cursor.fetchall()

        print("\n ==== PROFESSORES REGISTRADOS ==== ")

        for professor in professores:
            print(professor)
    except KeyboardInterrupt:
        print("operaçãp terminada, voltando ao menu...")

def atualizar_professores():
    try:
        ver_professores()

        print("\n ==== ATUALIZAR PROFESSORES ====")

        id_professor = int(input("qual o ID do professor que deseja atualizar?: "))

        cursor.execute(f"SELECT * FROM professores WHERE id_professor = {id_professor}")
        professor = cursor.fetchone()

        if not professor:
            print("não encontrado.")
            return
        nome = input("Qual o nome completo do professor? (obrigatório): ")
        telefone = input("Qual o telefone do professor? (obrigatório): ")
        materia = input("Qual a matéria do professor? (opcional): ")
        idade = int(input("Qual a idade do professor?(obrigatório): "))
        cpf = input("qual o CPF do professor? (obrigatório): ")
        salario = input("qual o salário atual do professor? (opcional): ")
        nome_colegio = input("qual o nome do colégio? (obrigatório): ")
        endereco = input("qual seu endereço? (obrigatorio): ")

        cursor.execute(f"UPDATE professores SET nome_professor = {nome}, idade_professor = {idade}, materia_professor = {materia}, salario_professor = {salario}, cpf_professor = {cpf}, nome_colegio = {nome_colegio}. endereco_professor = {endereco}, telefone_professor = {telefone}")
        print("professor atualizado com sucesso!")
        conexao.commit()

    except ValueError:
        print("erro de valor...")

    except NameError:
        print("erro de variavel...")
        print("buscando variavel...")
        print("variavel não encontrada!")

    except TypeError:
        print("objeto de tipo inadequado!")

    except IndexError:
        print("você tenta acessar um índice que não existe?")

    except KeyboardInterrupt:
        print("operaçãp terminada, voltando ao menu...")

def deletar_professores():
    try:
        ver_professores()

        print("\n ==== EXCLUIR PROFESSORES ====")

        idx = int(input("qual o ID do professor que deseja excluir?: "))

        cursor.execute("DELETE FROM professores WHERE id_professor = ?", (idx,))
        print("professor excluido com sucesso!")
        conexao.commit()
    
    except ValueError:
        print("erro de valor...")

    except NameError:
        print("erro de variavel...")
        print("buscando variavel...")
        print("variavel não encontrada!")

    except TypeError:
        print("objeto de tipo inadequado!")

    except IndexError:
        print("você tenta acessar um índice que não existe?")

    except KeyboardInterrupt:
        print("operaçãp terminada, voltando ao menu...")

def menu():
    while True:
        try:
            print("\n ==== MENU DO USUÁRIO ====")
            print("1 - Registrar Professores")
            print("2 - Ver Professores Registrados")
            print("3 - Atualizar Informações de Professores")
            print("4 - Deletar Professores Registrados")
            print("5 - sair")

            opcao = int(input("Qual opção vai escolher?: "))

            if opcao == 1:
                registrar_professores()
            elif opcao == 2:
                ver_professores()
            elif opcao == 3:
                atualizar_professores()
            elif opcao == 4:
                deletar_professores()
            elif opcao == 5:
                print("encerrando sistema...")
                conexao.close()
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
def menu():
    while True:
        try:
            print("\n ==== MENU DO USUÁRIO ====")
            print("1 - Registrar Professores")
            print("2 - Ver Professores Registrados")
            print("3 - Atualizar Informações de Professores")
            print("4 - Deletar Professores Registrados")
            print("5 - sair")

            opcao = int(input("Qual opção vai escolher?: "))

            if opcao == 1:
                registrar_professores()
            elif opcao == 2:
                ver_professores()
            elif opcao == 3:
                atualizar_professores()
            elif opcao == 4:
                deletar_professores()
            elif opcao == 5:
                print("encerrando sistema...")
                conexao.close()
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("erro de valor...")

        except NameError:
            print("erro de variavel...")
            print("buscando variavel...")
            print("variavel não encontrada!")

        except TypeError:
            print("objeto de tipo inadequado!")

        except IndexError:
            print("você tenta acessar um índice que não existe?")

        except KeyboardInterrupt:
            print("operaçãp terminada, voltando ao menu...")
menu()