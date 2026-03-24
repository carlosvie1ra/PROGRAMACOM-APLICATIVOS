autorizados = ["Alice", "Bob", "Carlos"]

nome = input("Digite o nome do pesquisador: ")

if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")
    
    confirmacao = input(f"Deseja remover {nome} da lista? (Sim/Não): ")
    if confirmacao == "sim":
        autorizados.remove(nome)
        print(f"Pesquisador removido. Lista atualizada: {autorizados}")
else:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")
    
    cadastro = input(f"Deseja cadastrar {nome} como novo pesquisador? (Sim/Não): ")
    if cadastro == "sim":
        autorizados.append(nome)
        print(f"Pesquisador cadastrado com sucesso! Lista atualizada: {autorizados}")