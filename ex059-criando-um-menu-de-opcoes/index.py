n1 = int(input('Primero número: '))
n2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa  ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}' .format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}' .format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior do que {}' .format(n1, n2))
        elif n2 > n1:
            print('{} é maior do que {}' .format(n2, n1))
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primero número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')

