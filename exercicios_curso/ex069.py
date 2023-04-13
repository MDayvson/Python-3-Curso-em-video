print('='*30)
print(f'{"CADASTRE UMA PESSOA":^30}')
print('='*30)

maior18 = qtdhomens = mulher20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: ').strip().upper()[0]

    if idade >= 18:
        maior18 += 1

    if sexo == 'M':
        qtdhomens += 1

    if sexo == 'F' and idade < 20:
        mulher20 += 1

    opção = ' '
    while opção not in 'SN':
        opção = input('Quer continuar [S/N] ').strip().upper()[0]
    if opção == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {qtdhomens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
