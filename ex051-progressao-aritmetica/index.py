print('=' * 30)
print('    10 TERMOS DE UMA PA     ')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo, razao):
    print('{}' .format(c), end=' -> ')
print('Acabou!')
