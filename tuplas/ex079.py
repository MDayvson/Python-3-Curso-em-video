lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')
