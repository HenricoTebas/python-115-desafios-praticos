from random import randint

computador = randint(0, 10)

print('''Sou seu computador...
Acabei de pensar em um número de 0 a 10.
Sera que você consegue adivinhar qual foi?''')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente. ')
        elif computador < jogador:
            print('Menos... Tente novamente. ')

print('Acertou com {} tentativas. Parabéns!' .format(palpites))

