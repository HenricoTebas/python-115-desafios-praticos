maior = homens = mulheres20 = 0
while True:
    print('-' * 23)
    print('  CADASTRE UM PESSOA  ')
    print('-' * 23)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 23)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheres20 += 1
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres menores de 20 anos.')

