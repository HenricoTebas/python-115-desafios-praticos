def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    if r['média'] >=7:
        r['situação'] = 'BOA'
    elif r['média'] >= 5:
        r['situação'] = 'RAZOÁVEL'
    else:
        r['situação'] = 'RUIM'
    return r


resp =notas(2.5,5.5,8,9.6,sit=True)
print(resp)