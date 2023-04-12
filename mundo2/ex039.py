import datetime

nasc = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual} ')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
elif idade > 18:
    print(f'Voce deveria ter se alistado há {idade - 18} anos. Seu alistamento foi em {nasc + 18}')
elif idade == 18:
    print('Voce deve se alistar imediatamente.')

