def fatorial(n, show=False):
    """
    ->Calcula o fatorial de um numero
    :parametro n: O numero a ser calculado
    :parametro show: (opcional) Mostrar ou nao a conta
    :return: O valor fatorial do numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))

help(fatorial)




