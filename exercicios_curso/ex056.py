soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = 0
tot_mulher20 = 0

for c in range(1, 5):
    print(f'{f" {c}° PESSOA ":=^20}')
    nome = input('NOME: ').strip().title()
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M/F]: ').strip().upper()

    soma_idade += idade

    if c == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        tot_mulher20 += 1


media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} ')
print(f'O homem mais velho tem {maior_idade_homem}anos e se chama {nome_velho}')
print(f'O número de mulheres com menos de 20 anos é {tot_mulher20}')
