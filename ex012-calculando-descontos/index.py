preco = float(input("Qual o preço do produto? R$ "))
desconto = preco - (preco * 5/100)

print("O produto que custa R${:.2f}, com o disconto de 5% vai custar R${:.2f}" .format(preco, desconto))