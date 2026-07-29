from menu import *
from admhos import admhos

while True:

    print('''
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
==============================================''')

    try:
        escolha = int(input('Qual a sua opção: '))

    except ValueError:
        print('\nOpção inválida! Digite apenas números.\n')
        continue

    if escolha == 1:
        admhos()

    elif escolha == 2:
        enfpro()

    elif escolha == 3:
        atmedico()

    elif escolha == 4:
        relatorio()

    elif escolha == 5:
        admsis()

    elif escolha == 6:
        print('\nSaindo do VittaCare...')
        break

    else:
        print('\nOpção inexistente! Tente novamente.\n')