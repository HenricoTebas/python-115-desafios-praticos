salario = float(input('Qual o valor do salário? R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}' .format(salario, novo))