numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Deseja continuar? [S/N]'))
    while r not in 'SsNn':
        r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print('-=' * 30)
print(f'Os valores digitados em ordem crescente são: {numeros}')

   