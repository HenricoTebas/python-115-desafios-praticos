distancia = float(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.' .format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
    print('O preço de sua passagem será R${:.2f}' .format(preco))

else:
    preco = distancia * 0.45
    print('O preço de sua passagem será R${:.2f}' .format(preco))

 