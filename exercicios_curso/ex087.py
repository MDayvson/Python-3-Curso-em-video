matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l}, {c}: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

    print()

print(f' A soma dos valores pares é {spar}')

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[l][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda coluna é {maior}')
