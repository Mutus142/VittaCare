setor = {}


def setores():

    while True:

        print("""
=========================================
          GESTÃO DE SETORES
=========================================

1 - Cadastrar setor
2 - Alterar setor
3 - Excluir setor
4 - Voltar

=========================================
Selecione uma opção:
=========================================
""")

        try:
            opcao = int(input("Selecione uma opção: "))

        except ValueError:
            print("\nOpção inválida!")
            continue

        if opcao == 1:
            cadastrar_setor()

        elif opcao == 2:
            alterar_setor()

        elif opcao == 3:
            excluir_setor()

        elif opcao == 4:
            print("\nVoltando...")
            break

        else:
            print("\nOpção inválida!")


def cadastrar_setor():

    nome_setor = input("Qual é o nome do setor? ").lower()

    try:
        andar_setor = int(input("Qual é o andar do setor? "))

    except ValueError:
        print("\nO andar deve ser um número!")
        return

    if nome_setor in setor:
        print("\nSetor já cadastrado!")

    else:

        setor[nome_setor] = {
            "nome": nome_setor,
            "andar": andar_setor
        }

        print("\nSetor cadastrado com sucesso!")


def alterar_setor():

    nome_setor = input("Qual é o nome do setor? ").lower()

    if nome_setor in setor:

        nome_novo = input("Qual é o novo nome do setor? ").lower()

        setor[nome_novo] = setor.pop(nome_setor)
        setor[nome_novo]["nome"] = nome_novo

        alterar_andar = input(
            "Deseja alterar o andar do setor? (S/N): "
        ).upper()

        if alterar_andar == "S":

            try:
                novo_andar = int(input("Qual é o novo andar? "))

            except ValueError:
                print("\nAndar inválido!")
                return

            setor[nome_novo]["andar"] = novo_andar

        print("\nSetor alterado com sucesso!")

    else:
        print("\nSetor não encontrado!")


def excluir_setor():

    nome_setor = input(
        "Qual é o nome do setor que deseja excluir? "
    ).lower()

    if nome_setor in setor:

        confirmacao = input(
            "Você tem certeza dessa operação? (S/N): "
        ).upper()

        if confirmacao == "S":

            del setor[nome_setor]
            print("\nSetor removido com sucesso!")

        elif confirmacao == "N":

            print("\nOperação cancelada!")

        else:

            print("\nOpção inválida!")

    else:

        print("\nSetor não encontrado!")