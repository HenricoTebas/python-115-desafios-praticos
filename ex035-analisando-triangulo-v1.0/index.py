print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo.')
else:
    print('Os seguimentos acima NÂO PODEM FORMAR um triângulo.')