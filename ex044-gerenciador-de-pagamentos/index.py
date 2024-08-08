preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista no cartão
      [3] em até 2x no cartão
      [4] 3x ou mais no cartão''')

opcao = int(input('Qual a opção?'))

if opcao == 1:
    total = preco - (preco * (10/100))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * (5/100))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
elif opcao == 3:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, preco))
elif opcao == 4:
    total = preco + (preco * (20/100))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
else:
    print('Opção inválida!')
    

