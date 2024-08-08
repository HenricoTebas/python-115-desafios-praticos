n = int(input('Digite um número inteiro: '))
resultado = n % 2

if resultado == 0:
    print('O numero {} é PAR' .format(n))
else:
    print('O número {} é ÍMPAR' .format(n))