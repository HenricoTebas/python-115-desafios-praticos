def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.

    Args:
        preco (int, optional): O preço que se quer reajustar.
        taxa (int, optional): Qual é a porcentagemdo aumento.
        formato (bool, optional): Quer a saída formatada ou não.

    Return: O valor reajustado com ou sem formato.
        
    """
    resp = preco + (preco * (taxa/100))
    return resp if formato is False else moeda(resp)


def diminuir(preco=0, taxa=0, formato=False):
    resp = preco - (preco * (taxa/100))
    return resp if formato is False else moeda(resp)


def dobro(preco=0, formato=False):
    resp = preco * 2
    return resp if not formato else moeda(resp)
    

def metade(preco=0, formato=False):
    resp = preco / 2
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='R$', formato=False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 35)
    
