import random
import time
import operator
jogo = {}

for cont in range(1, 5):
    jogo[f'jogador {cont}'] = random.randint(1, 6)

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)

ranking = []
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-='*30)
print(f'{"  RANKING DOS JOGADORES  ":=^30}')
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}.')
    time.sleep(1)
