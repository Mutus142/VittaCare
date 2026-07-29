from Usuarios.usuarios import usuarios
from Services.setores import setores
from Pacientes.cadastropaciente import pacientes


def admhos():

    while True:

        print("""
==================================
    ADMINISTRAÇÃO HOSPITALAR
==================================

1 - Gestão de Pacientes
2 - Gestão de Usuários
3 - Gestão de Setores
4 - Voltar

==================================
""")

        try:
            escolha = int(input("Selecione uma opção: "))

        except ValueError:
            print("\nOpção inválida!")
            continue

        if escolha == 1:
            pacientes()

        elif escolha == 2:
            usuarios()

        elif escolha == 3:
            setores()

        elif escolha == 4:
            print("\nVoltando ao menu principal...\n")
            break

        else:
            print("\nOpção inválida!\n")