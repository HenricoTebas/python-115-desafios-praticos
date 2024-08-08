def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é {a:.2f}m².')



print(' Controle de Terreno ')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)