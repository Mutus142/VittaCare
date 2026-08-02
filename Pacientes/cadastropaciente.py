from DataBase.conexao import conexao, cursor

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
        setor = input("Qual o setor do paciente? ").lower()
        idade = int(input("Qual a idade do paciente? "))

        sql = """
        INSERT INTO pacientes
        (nome_paciente, idade, setor)

        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (nome, idade, setor))
        conexao.commit()

        print("Paciente cadastrado!")

def localizar():

    nome = input('Qual o nome do paciente que deseja procurar? ').lower()

    sql = """
    SELECT nome_paciente, idade, setor
    FROM pacientes
    WHERE nome_paciente = %s
    """

    cursor.execute(sql, (nome,))

    paciente = cursor.fetchone()

    if paciente:

        print(f"""
Nome: {paciente[0]}
Idade: {paciente[1]}
Setor: {paciente[2]}
""")

    else:
        print("Paciente não encontrado!")

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