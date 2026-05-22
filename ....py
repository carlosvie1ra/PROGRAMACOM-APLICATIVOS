import json #salvar ou carregar dados
import os #permite ao Python interagir com o sistema operacional.

BANCO_DADOS = 'alunos.json' #adiciona o arquivo JSON em uma variavel

def cadastrar(): #cria a variavel que sera adicionada no menu
    print("\n--- Novo Cadastro ---") #mostra no terminal para começar o modelo de menu
    
    if os.path.exists(BANCO_DADOS): #serve para verificar se o arquivo ou pasta do banco de dados já existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F
            alunos = json.load(f) #adiciona a nova variavel junto do arquivo
    else:
        alunos = [] #garante que caso seja ao contrario do if pare, ou caso o proposito do if ja seja cumprido

    novo_aluno = { #variavel criada para cadastrar os dados do aluno
        "nome": input("Nome: "),  #pedir o nome ao usuario
        "telefone": input("Telefone: "), #pedir o telefone
        "turma": input("Turma: "), #pedir turma
        "idade": int(input("Idade: ")), #pedir idade
        "cpf": input("CPF: ") #pedir o cpf
    }
    
    alunos.append(novo_aluno) #adicionar o aluno no ultimo lugar da lista

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e escrever dentro do arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False) #salva uma lista ou dicionário de dados em um arquivo de texto no formato JSON
        
    print("Aluno cadastrado com sucesso!") #informa que o aluno foi cadastrado

def listar(): #cria a variavel que sera adicionada no menu
    print("\n--- Lista de Alunos ---")
    
    if os.path.exists(BANCO_DADOS): #serve para verificar se o arquivo ou pasta do banco de dados já existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e ler dentro do arquivo
            alunos = json.load(f) #adiciona a nova variavel junto do arquivo
    else:
        alunos = [] #caso contrario alunos = lista

    if not alunos: 
        print("Nenhum aluno cadastrado.") #informa que nenhum aluno esta cadastrado
        return #retorna ao menu

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") #vai procurar o item aluno dentro da lista e mostrar junto no nome as informações adicionadas

def atualizar(): #cria a variavel que sera adicionada no menu
    print("\n--- Atualizar Aluno ---") #informa que o aluno vai ser adicionado
    if not os.path.exists(BANCO_DADOS): #verifica se o banco de dados NÃO existe.
        print("Nenhum aluno cadastrado no sistema.") #se não tiver nenhum aluno ja cadastrado ira mostrar o print 
        return #retorna ao menu

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e ler dentro do arquivo
        alunos = json.load(f) #adiciona a nova variavel junto do arquivo
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ") #informar o cpf do aluno que deseja atualizar
    
    for aluno in alunos: # Percorre a lista de alunos, um por um
        if aluno['cpf'] == cpf_busca:  # Checa se o CPF do aluno atual é igual ao CPF que está sendo buscado
            print(f"Editando dados de: {aluno['nome']}") # Exibe na tela o nome do aluno que será editado
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # Pede o novo nome; se o usuário der Enter em branco (vazio), mantém o nome atual
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] # Pede o novo telefone; se der Enter em branco, mantém o telefone atual
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # Pede a nova turma; se der Enter em branco, mantém a turma atual
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) # Pede a nova idade, mantém a atual se em branco, e converte o texto para número inteiro (int)
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] # Pede o novo CPF; se der Enter em branco, mantém o CPF atual
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e escrever dentro do arquivo
                json.dump(alunos, f, indent=4, ensure_ascii=False) # Salva a lista completa e atualizada dentro do arquivo em formato JSON organizado
            print("Dados atualizados com sucesso!") #informa que os dados foram atualizados
            return #retorna ao menu
            
    print("Aluno não encontrado.") #informa que o aluno não foi encontrado

def excluir(): #cria a variavel que sera adicionada no menu
    print("\n--- Excluir Aluno ---") #moldura para o menu
    if not os.path.exists(BANCO_DADOS): #verifica se o banco de dados NÃO existe.
        print("Nenhum aluno cadastrado no sistema.")  #informa qur não a nenhum aluno cadastrado no cinema
        return #retorna ao menu

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e ler dentro do arquivo
        alunos = json.load(f) #adiciona a nova variavel junto do arquivo
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ") #pede o cpf adicionada anteriormente para excluir o usuario
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca] #vai procurar o item dentro da lista(arquivo), depois pegara o item buscado pelo cpf
    
    if len(nova_lista) < len(alunos): #ler a nova lista e ler os alunos vendo se e menor que a lista
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e escrever dentro do arquivo
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # Salva a nova lista atualizada (sem o aluno removido) no arquivo JSON de forma organizada
        print("Aluno removido com sucesso!") # Exibe uma mensagem confirmando que a exclusão deu certo
    else:
        print("Aluno não encontrado.") # Exibe uma mensagem informando que o aluno buscado não está cadastrado

def menu(): #cria a variavel que sera adicionada no menu
    if not os.path.exists(BANCO_DADOS): #verifica se o banco de dados NÃO existe.
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #abre o arquivo e le em portugues adicionando na variavel F e escrever dentro do arquivo
            json.dump([], f) # Cria ou limpa o arquivo salvando uma lista vazia ([]) em formato JSON

    while True:
        print("\n=== SISTEMA ESCOLAR ===") #mostra no terminal para começar o modelo de menu
        print("1. Cadastrar Aluno") #informar o que da pra fazer no menu (opção)
        print("2. Listar Alunos") #informar o que da pra fazer no menu (opção)
        print("3. Atualizar Aluno") #informar o que da pra fazer no menu (opção)
        print("4. Excluir Aluno") #informar o que da pra fazer no menu (opção)
        print("5. Sair") #informar o que da pra fazer no menu (opção)
        
        opcao = input("Escolha uma opção: ") #pergunta ao usuario qual opção acima deseja
        
        if opcao == '1': cadastrar() #serve como um pistao inicial para rodar o codigo da def variavel cadastrar
        elif opcao == '2': listar() #serve como um pistao inicial para rodar o codigo da def variavel listar
        elif opcao == '3': atualizar() #serve como um pistao inicial para rodar o codigo da def variavel atualizar
        elif opcao == '4': excluir() #serve como um pistao inicial para rodar o codigo da def variavel excluir
        elif opcao == '5': break  ##serve como um pistao inicial para dizer para o programa parar
        else: print("Opção inválida!") #caso nãp seja nenhuma das opções pergunta novamente

menu() #menu