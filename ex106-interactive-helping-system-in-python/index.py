c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m', # 1 - vermelho 
     '\033[030;42m',  # 2 - verde
     '\033[030;43m',  # 3- amarelo
     '\033[030;44m',  # 4 - azul
     '\030[030;45m',  # 5 - roxo
     '\030[7;030m'    # 6 - branco
     ),



def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)