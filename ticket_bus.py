import os
import datetime 

continua = True
assentos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
mensagem1 = 'Opção Inválida. Tente Novamente'

altura = 24
# Para limpar o Terminal
# os.system('clear')

qtde_assentos = 52

def menu():
    agora = datetime.datetime.now()
    texto = agora.strftime("                                 Ticket System                         %H:%M:%S ")
    print(texto)

    print("\n\n\n1 - Comprar ticket\n\n2 - Partir onibus\n\n3 - Alterar quantidade de assentos\n\n4 - Monetario\n\nX - Fechar programa\n\n")
    resp = input("\n\n\n\n\n\n\n\nDigite uma dessas opções: ")
    
    return resp


def menu_compra():
    agora = datetime.datetime.now()
    texto = agora.strftime("                                 Ticket System                         %H:%M:%S ")
    print(texto)
    
    print('\n\nEscolha seu assento\n\n')
    print(assentos)
    resp2 = input("\n\n\n\n\n\n\n\n\nEscolha uma opção: ")

    if resp2 == 'x' or resp2 == 'X':
        exit()
    elif resp2 == 'b' or resp2 == 'B':
        print('Voltar para o menu anterior')
    elif resp2.isnumeric and int(resp2) > 0 and int(resp2) <= qtde_assentos:
        escolha_assento = int(resp2)
        indice = int(resp2) - 1
        if escolha_assento < 1 or escolha_assento > qtde_assentos:
            print('Assento nao encontrado. Tente Novamente')
            escolha_assento = input("\n\nDigite o assento escolhido: ")
        else:
            for escolha_assento in assentos:
                assentos[indice] = "X"
                print(assentos)
                break
    else:
        print('Assento nao encontrado. Tente novamente')
    
        
#def partir_onibus():
  
#main
while continua:
     
    resp = menu()
    os.system('clear')
    if resp != "1" and resp != "2" and resp != "3" and resp != "4" and resp != "x" and resp != "X":
        os.system('clear')
        print(mensagem1)
    elif resp == "1":
        menu_compra()
        print('Compra do ticket realizada')
    elif resp == "2":
        print('.')
        #partir_onibus()
    elif resp == "3":
        print("Alterar quantidade de assentos")
    elif resp == "4":
        print("Monetario")
    else:
        continua = False