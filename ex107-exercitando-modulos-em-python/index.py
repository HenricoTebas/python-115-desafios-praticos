import moeda

num = float(input('Digite o preço: R$'))

print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num, 10)}')
print(f'Diminuindo em 10%, temos R${moeda.diminuir(num, 10)}')
