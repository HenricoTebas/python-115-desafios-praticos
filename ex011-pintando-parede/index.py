larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt 
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.3f}m².' .format(larg, alt, area)) 
print('Para pintar essa parede, você precisará de {}l de tinta' .format(tinta))