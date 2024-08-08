lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]'))
    lista.sort(reverse=True)
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
if 5 in lista:
    print('O Valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são: {lista}')