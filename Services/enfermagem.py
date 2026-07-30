



def enfermagem():

    while True:
            print('''
=========================================
      ENFERMAGEM E PRONTUÁRIOS
=========================================

1 - Localizar paciente
2 - Registrar sinais vitais
3 - Evolução de enfermagem
4 - Dar alta hospitalar
5 - Voltar

=========================================
Selecione uma opção:
=========================================''')

            try:
                opcao = int(input('Selecione uma opção: '))

            except ValueError:
                print('Opção invalida!')

                if opcao == 1:
                    localizar()

                elif opcao == 2:
                     sinais_vitais()

                elif opcao == 3:
                     evo_paciente()

                elif opcao == 4:
                     alta()

                elif opcao == 5
                    print('Voltando...')
                    break

                else:
                     print('Opção invalida!')

                