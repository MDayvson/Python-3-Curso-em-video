lista_tot = []
lista_pares = []
lista_impares = []
while True:
    num = int(input('Digite um número: '))

    lista_tot.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é {lista_tot}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')

