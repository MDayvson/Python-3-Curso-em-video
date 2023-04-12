import datetime

ano_atual = datetime.date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c} pessoa nasceu? '))
    if (ano_atual - nasc) < 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {menor} pessoas menores de idade')
print(f'E tambem {maior} pessoas maiores de idade')
