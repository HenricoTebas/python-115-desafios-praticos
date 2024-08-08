total = caro = menor = cont = 0
barato = ''
while True:
    print('-' * 30)
    print('  LOJA SUPER BARATÃO  ')
    print('-' * 30)
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi: R${total:.2F}')
print(f'Temos {caro} produto custando mais de R$1000.00')
print(f'O pruduto mais barato foi {barato} que custa {menor:.2f}')

    
