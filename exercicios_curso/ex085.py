lista = [[], []]

for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(lista)

lista[0].sort()
lista[1].sort()

print(f'A lista dos pares é {lista[0]}')
print(f'A lista dos impares é {lista[1]}')
