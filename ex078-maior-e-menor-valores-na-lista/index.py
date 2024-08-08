maior = menor = 0
num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um númerona pisoção {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print(f'O maior valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')




