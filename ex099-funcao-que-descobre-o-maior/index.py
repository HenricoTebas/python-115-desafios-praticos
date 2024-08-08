from time import sleep
def maior(*num):
    print('-=' * 30)
    cont = maior = 0
    print('Analisando os valores passados..')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(9, 8, 4, 0, 3)
maior(6, 5, 0)
maior(1, 2)
maior()