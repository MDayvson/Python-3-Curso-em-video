import random
import time

numeros = []


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for cont in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        time.sleep(0.5)
    print()


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} temos: {soma}')


sorteia(numeros)
somapar(numeros)
