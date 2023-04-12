import random
import time

lista = []
jogos = []

print(f'{" Sorteio Mega sena ":=^30}')
quant = int(input('Quantos jogos quer jogar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    time.sleep(2)
