lista = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores adcionados foram {lista}')
