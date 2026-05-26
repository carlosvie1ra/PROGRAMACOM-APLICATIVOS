import json
import os

dados = "alunos.json"

def cadastrar_aluno():
    print("\n ---- NOVO ALUNO ----")
    
    if os.path.exists(dados):
        with open(dados, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []
    
    aluno = { 
        "nome": input("Nome: "),  
        "telefone": input("Telefone: "), 
        "turma": input("Turma: "), 
        "idade": int(input("Idade: ")), 
        "cpf": int(input("CPF: ")),
        "id": input("id:").
     }

    alunos.append(aluno)

    with open(dados, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4)

        print("Aluno cadastrado com sucesso!")
cadastrar_aluno()