import datetime

pessoa = {}

pessoa['Nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: ').strip())

hoje = datetime.datetime.today().year

pessoa['Idade'] = hoje-nascimento
ctps = int(input('Carteira de Trabalho: (0 não tem): '))
if ctps != 0:
    pessoa['CTPS'] = ctps
    pessoa['contratação'] = int(input('Ano de contratação: ').strip())
    pessoa['Salário'] = float(input('Salário: ').strip())
    pessoa['aposentadoria'] = pessoa['Idade'] + ((pessoa['contratação'] + 35) - hoje)
else:
    print('FIM')
print('-='*30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
