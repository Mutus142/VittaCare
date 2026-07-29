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
            alterar_setor()

        elif opcao == "4":
            remover_paciente()

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

    if paciente[nome]["nome"]:

        print(f"""
        Nome: {paciente[nome]["nome"]}
        Setor: {paciente[nome]["setor"]}
        Idade: {paciente[nome]["idade"]}
        """)

    else:
        print('Paciente não encontrado!')

def alterar_setor():

    nome = input('Qual o nome do paciente que deseja alterar? ').lower()

    if nome in paciente:
        setor = input('Qual é o novo setor? ')

        paciente[nome]["setor"] = setor
        print('Setor alterado! ')

    else:
        print('Paciente não encontrado!')

def remover_paciente():

    nome = input("Qual é o nome do paciente? ").lower()

    if nome in paciente:

        confirmacao = input("Tem certeza que deseja remover este paciente? (S/N): ").upper()

        if confirmacao == "S":

            del paciente[nome]
            print("\nPaciente removido com sucesso!")

        elif confirmacao == "N":

            print("\nOperação cancelada!")

        else:

            print("\nOpção inválida!")

    else:
        print("\nPaciente não encontrado!")