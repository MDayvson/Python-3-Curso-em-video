lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break
lista.sort(reverse=True)
print(f'Voçê digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não foi encontrado na lista')
