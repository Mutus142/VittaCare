paciente = {}


def pacientes():

    while True:

        print("""
=============================
     GESTÃO DE PACIENTES
=============================

1 - Cadastrar paciente
2 - Localizar paciente
3 - Alterar setor
4 - Excluir paciente
5 - Voltar

=============================
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastro()

        elif opcao == "2":
            localizar()

        elif opcao == "3":
            print("Alteração de setor em desenvolvimento.")

        elif opcao == "4":
            print("Exclusão em desenvolvimento.")

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")


def cadastro():

    nome = input("Qual é o nome do paciente? ").lower()
    setor = input("Qual o setor do paciente? ")
    idade = int(input("Qual a idade do paciente? "))

    if nome in paciente:
        print("Paciente já cadastrado!")

    else:
        paciente[nome] = {
            "nome": nome,
            "setor": setor,
            "idade": idade
        }

        print("Paciente cadastrado!")

def localizar():

    nome = input('Qual o nome do paciente que deseja procurar? ').lower()

    for nome in paciente:
        setor = paciente[setor]
        idade = paciente[idade]

        print(f'''
        Nome: {nome}
        Setor: {setor}
        Idade: {idade}''')

    else:
        print('Paciente não encontrado!')