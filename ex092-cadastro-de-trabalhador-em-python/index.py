from datetime import datetime
pessoa = {}

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.now().year)
        

print('-=' * 30)
for k, v in pessoa.items():
            print(f'{k} tem o valor {v}')
        

    

