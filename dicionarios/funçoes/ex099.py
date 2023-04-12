import time


def maior(*num):
    print('-=' * 20)
    print('Analizando os valores passados...')

    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=' ')

        time.sleep(0.5)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
