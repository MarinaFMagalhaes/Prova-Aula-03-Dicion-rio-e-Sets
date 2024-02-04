'''Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de 
matrícula usando um dicionário.
O programa deve fornecer as seguintes funcionalidades:
Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, 
exibindo seus respectivos números de matrícula.
O programa deve ser executado em um loop contínuo até que o usuário escolha sair.'''

alunos = {}
cadastramento = True

while cadastramento:
    print("\n1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar alunos")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        alunos[matricula] = nome
        print("Aluno adicionado!")

    elif escolha == "2":
        matricula = input("Digite o número de matrícula do aluno a ser removido: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Aluno removido!")
        else:
            print("Aluno não encontrado.")

    elif escolha == "3":
        if alunos:
            print("\nLista de alunos:")
            for matricula, nome in alunos.items():
                print(f"{matricula}: {nome}")
        else:
            print("Nenhum aluno cadastrado.")

    elif escolha == "4":
        print("Cadastramento finalizado. Saindo do programa.")
        cadastramento = False

    else:
        print("Opção inválida. Tente novamente.")
