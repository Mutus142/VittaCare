from Pacientes.cadastropaciente import paciente


sinais = {}
evo = {}

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

                elif opcao == 5:
                    print('Voltando...')
                    break

                else:
                     print('Opção invalida!')


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

def sinais_vitais():

    nome = input('Qual o nome do paciente?').lower()

    if nome in paciente:
        temperatura = int(input('Qual é a temperatura do paciente?'))
        fq_car = int(input('Qual é a frequencia cardiaca do paciente?'))
        fq_resp = int(input('Qual é a frequencia respiratoria do paciente?'))

        sinais[nome] = {
            "temperatura": temperatura,
            "fq_car": fq_car,
            "fq_resp": fq_resp
        }

    else:
        print('Paciente não encontrado!')


def evo_paciente():

    nome = input('Qual é o nome do paciente? ').lower()

    if nome in paciente:
        evo_pac = input('Qual é a evolução do paciente? ')

        evo[nome] = {
            "evo_pac": evo_pac
        }

    else:
        print('Paciente não encontrado!')


def alta():

    nome = input('Qual o nome do paciente? ')

    if nome in paciente:
        alta_con = input('Voce quer dar alta para esse paciente? S/N ').upper()

        if alta_con == 'S':
            print('Agora esse paciente está com alta!')

        elif alta_con == 'N':
            print('Alta cancelada!')

        else:
            print('Opção invalida!')