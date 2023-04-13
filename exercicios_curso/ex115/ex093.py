import time

jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for cont in range(1, tot + 1):
    gols.append(int(input(f'    Quantos gols na partida {cont}? ')))

jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["Nome"]} jogou {tot} partidas.')
for i, p in enumerate(jogador['Gols']):
    print(f'   => Na partida {i + 1}, fez {p} gols.')
    time.sleep(1)
print('-=' * 30)
