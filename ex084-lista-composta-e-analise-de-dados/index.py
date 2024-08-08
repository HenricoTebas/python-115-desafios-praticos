pessoas = []
lista = []
maiorp = menorp = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(lista) == 0:
        maiorp = menorp = pessoas[1]
    else:
        if pessoas[1] > maiorp:
            maiorp = pessoas[1]
        if pessoas[1] < menorp:
            menorp = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N]'))
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'O total de pessoas cadastradas é {len(lista)}')
print(f'O maior peso foi de {maiorp}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end ='')
print()
print(f'O menor peso foi de {menorp}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menorp:
        print(f'[{p[0]}]', end='')

