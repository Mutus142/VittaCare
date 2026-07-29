from Services.admhos import admhos


def menu_principal():

    while True:

        print("""
==============================================
            VittaCare v0.1
    Sistema Integrado de Gestão Hospitalar
==============================================

            MENU PRINCIPAL

    1 - Administração Hospitalar
    2 - Enfermagem e Prontuários
    3 - Atendimento Médico
    4 - Relatórios
    5 - Configurações do Sistema
    6 - Sair

==============================================
        Selecione uma opção:
==============================================
""")

        try:
            escolha = int(input("Qual a sua opção: "))

        except ValueError:
            print("\nOpção inválida!")
            continue

        if escolha == 1:
            admhos()

        elif escolha == 6:
            print("\nSaindo do VittaCare...")
            break

        else:
            print("\nEssa funcionalidade ainda não foi implementada.\n")