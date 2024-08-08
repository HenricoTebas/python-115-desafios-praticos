count = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'A soma dos {count} é {soma}!')