pessoa = {}
cadastro = []

tot_pessoas = soma_idade = media_idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))

    tot_pessoas += 1  # Pessoas cadastradas
    soma_idade += pessoa['idade']  # Média de Idade

    cadastro.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print(f'A) Ao todo temos {tot_pessoas} pessoas cadastradas.')

media_idade = soma_idade / tot_pessoas
print(f'B) A média de idade é de {media_idade:5.2f} anos.')

print(f'C) As mulheres cadastradas foram: ', end=' ')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]},', end=' ')
print()

print(f'D) Lista de pessoas que estão acima da média: ')
for p in cadastro:
    if p['idade'] >= media_idade:

        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('FIM')
