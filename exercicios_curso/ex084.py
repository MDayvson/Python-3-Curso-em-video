cadastro = []
pessoa = []
maior_peso = menor_peso = 0

while True:
    pessoa.append(str(input('Nome: ')).strip().title())
    pessoa.append(float(input('Peso: ').strip()))

    if len(cadastro) == 0:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]

    cadastro.append(pessoa[:])
    pessoa.clear()

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break
print(cadastro)
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso foi de {maior_peso}KG. Peso de : ', end='')
for p in cadastro:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end='')
print()

print(f'O menor peso foi de {menor_peso}KG. peso de: ', end='')
for p in cadastro:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end='')

