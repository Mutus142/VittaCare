funcionario = {}


def funcionarios():

    while True:

        print("""
=========================================
       GESTÃO DE FUNCIONÁRIOS
=========================================

1 - Cadastrar funcionário
2 - Alterar cargo
3 - Excluir funcionário
4 - Localizar funcionário
5 - Listar funcionários
6 - Voltar

=========================================
Selecione uma opção:
=========================================
""")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastro()

        elif opcao == "2":
            alterar_cargo()

        elif opcao == "3":
            remover_funcionario()

        elif opcao == "4":
            localizar()

        elif opcao == "5":
            listar()

        elif opcao == "6":
            break

        else:
            print("\nOpção inválida!\n")


def cadastro():

    nome = input("Qual é o nome do funcionário? ").lower()
    cargo = input("Qual é o cargo do funcionário? ").lower()
    setor = input("Qual é o setor do funcionário? ").lower()

    if nome in funcionario:
        print("\nFuncionário já cadastrado!")

    else:

        funcionario[nome] = {
            "nome": nome,
            "cargo": cargo,
            "setor": setor
        }

        print("\nFuncionário cadastrado com sucesso!")

def alterar_cargo():

    nome = input('Qual é o nome do funcionario? ').lower()

    if nome in funcionario:
        cargo_novo = input('Qual o cargo novo? ').lower()

        funcionario[nome]["cargo"] = cargo_novo
        print('Cargo alterado!')

    else:
        print('Funcionario não encontrado!')

def remover_funcionario():

    nome = input("Qual é o nome do funcionário? ").lower()

    if nome in funcionario:

        confirmacao = input("Tem certeza que deseja remover este funcionário? (S/N): ").upper()

        if confirmacao == "S":

            del funcionario[nome]
            print("\nFuncionário removido com sucesso!")

        elif confirmacao == "N":

            print("\nOperação cancelada!")

        else:

            print("\nOpção inválida!")

    else:
        print("\nFuncionário não encontrado!")