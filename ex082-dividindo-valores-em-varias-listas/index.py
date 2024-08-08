lista = []
pares = []
impares = []
while True:
    n = ((int(input('Digite um valor: '))))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Deseja continuar? [S/N]'))
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A lsita completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')

