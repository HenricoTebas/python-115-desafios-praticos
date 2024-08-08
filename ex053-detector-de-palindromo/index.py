frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

'''for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]'''

print('O iverso de {} é {}.' .format(junto, inverso))
if inverso == junto:
        print('Temos um PALÍNDROMO!')
else:
        print('A frase digitada NÃO É UM PALÍNDROMO!')


