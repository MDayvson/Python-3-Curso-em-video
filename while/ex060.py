n = int(input('''Digite um número para
calcular seu Fatorial: '''))
cont = n
f = 1
while cont > 0:
    print(f'{cont}', end='')
    f *= cont
    cont -= 1
    if cont >= 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(f)
