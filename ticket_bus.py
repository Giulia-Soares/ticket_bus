import os
import datetime 

#TODO: Criar tela de quantidade de assentos.
#       Usar mesmo layout das telas do sistema.
#       Deve apresentar a quantidade atual de assentos.
#       Permitir alterar para entre 30 e 80 assentos por ônibus.
#       Mesmos comandos para voltar e fechar.

#TODO: Criar tela de monetário.
#       Usar mesmo layout das telas do sistema.
#       Deve apresentar em R$.
#       Deve apresentar o valor atual (default = 5,20).
#       Deve apresentar total de vendas para onibus atual.
#       Deve apresentar total de vendas geral.
#       Permitir alteracao do valor da passagem.
#       Mesmos comandos para voltar e fechar.


# 0 = menu
# 1 = menu compra
# 2 = Alterar quantidade de assentos
# 3 = Monetario

continua = True
assentos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
mensagem = ""
screen_flag = 0
qtde_assentos = 52

def partir_onibus():
    assentos = []
    for i in range(qtde_assentos):
        assentos.append(i + 1)

    return assentos

def menu():

    global mensagem, screen_flag, assentos

    agora = datetime.datetime.now()
    texto = agora.strftime("                                 Ticket System                         %H:%M:%S ")
    
    os.system('clear')

    print(texto)
    print("\n\n\n1 - Comprar ticket")
    print("\n2 - Partir onibus")
    print("\n3 - Alterar quantidade de assentos")
    print("\n4 - Monetario\n")
    print("X - Fechar programa\n")

    print(f"\n\n\n\n\n\n\n{mensagem.upper()}")

    option = input("Digite uma dessas opções: ")

    if option.lower() == 'x':
        os.system('clear')
        exit()

    if option.isnumeric():
        if option == "1":
            screen_flag = 1
            return
        elif option == "2":
            assentos = partir_onibus()
            mensagem = 'Onibus partiu! Assentos para a proxima viagem ja disponiveis!'
        elif option == "3":
            mensagem = 'Tela para alterar quantidade de assentos nao implementada'
        elif option == '4':
            mensagem = 'Tela do Monetario nao implementada'
        else:
            mensagem = 'Tela inexistente'
    else:
        os.system('clear')
        mensagem = 'opcao invalida'

def menu_compra():

    global mensagem, screen_flag, assentos

    agora = datetime.datetime.now()
    texto = agora.strftime("                                 Ticket System                         %H:%M:%S ")

    os.system('clear')

    print(texto)
    print('\n\nEscolha seu assento\n')
    print(assentos)

    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n{mensagem.upper()}")

    option = input("Escolha uma opção: ")

    if option.lower() == 'x':
        os.system('clear')
        exit() 
    elif option.lower() == 'b':
        screen_flag = 0
        return

    if option.isnumeric():  
        option = int(option)
        if option > 0 and option <= qtde_assentos:
            i = option -1
            assentos[i] = 'X'
            print(assentos)
            mensagem = f'assento de numero {option} escolhido'
        else:
            mensagem = 'assento inexistente'
    else:
        mensagem = 'opcao invalida'
  
#main
while continua:

        if screen_flag == 0:
            menu()
        elif screen_flag == 1:
            menu_compra()
        elif screen_flag == 2:
            mensagem = 'Tela Indisponivel'
        elif screen_flag == 3:
            mensagem = 'Tela indisponivel'
        else:
            mensagem = 'Tela inexistente'
