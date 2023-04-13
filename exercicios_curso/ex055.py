maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c} pessoa: '))

    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f'O menor peso lido foi de {menor} kg')
print(f'O maior peso lido foi de {maior} kg')
