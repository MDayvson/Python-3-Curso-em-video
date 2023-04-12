import random
import time

opções = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)

print(f'{" JOKENPÔ ":=^30}')
jogador = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual a sua jogada? '''))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
print('='*30)
print(f'O computador jogou {opções[computador]}')
print(f'O jogador jogou {opções[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
print('='*30)