peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é {:.1f}.' .format(imc))

if imc <= 18.5:
    print('Você está na faixa de ABAIXO DO PESO!')
elif imc <= 25:
    print('PARABÉNS! Você está na faixa de PESO IDEAL!')
elif imc <= 30:
    print('Você está na faixa de SOBREPESO!')
elif imc <= 40:
    print('Você está na faixa de OBESIDADE!')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA!')