setores = {}


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

    andar_setor = int(input("Qual é o andar do setor? "))

    if nome_setor in setores:
        print("\nSetor já cadastrado!")

    else:

        setores[nome_setor] = {
            "nome": nome_setor,
            "andar": andar_setor
        }

        print("\nSetor cadastrado com sucesso!")


def alterar_setor():

    nome_setor = input("Qual é o nome do setor? ").lower()

    if nome_setor in setores:

        nome_novo = input("Qual é o novo nome do setor? ").lower()

        setores[nome_setor]["nome"] = nome_novo

        andar_novo = input(
            "Você quer alterar o andar do setor? (S/N): "
        ).upper()

        if andar_novo == "S":

            novo_andar = int(
                input("Qual é o novo andar? ")
            )

            setores[nome_setor]["andar"] = novo_andar

        elif andar_novo == "N":

            print("\nOperação concluída!")

        else:

            print("\nOpção inválida!")

    else:
        print("\nSetor não cadastrado!")


def excluir_setor():

    nome_setor = input('Qual é o nome do setor que deseja excluir? ')

    if nome_setor in setores:
        confirmacao = input('Voce tem certeza dessa operação? ').upper()

        if confirmacao == 'S':
            del setores[nome_setor]
            print('Removendo setor...')

        elif confirmacao == 'N':
            print('Operação cancelada!')

        else:
            print('Opção invalida!')

    else:
        print('Setor não encontrado!')