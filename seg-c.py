
curso = input("Você concluiu o Curso de Segurança? (s/n): ")

if curso == 'n':
    print("Acesso Negado: Faça o treinamento primeiro")
elif curso == 's':

    instrutor = input("O Instrutor está presente na sala? (s/n): ")
    
    if instrutor == 's':
        print("Acesso Liberado: Operação iniciada")
    else:
        print("Aguarde o instrutor para ligar a máquina")
else:
    print("Opção inválida. Responda apenas com 's' ou 'n'.")
