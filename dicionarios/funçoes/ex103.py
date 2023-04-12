def ficha(nome='<desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gols no campeonato.')


n = str(input('Nome do jogador: ')).strip().title()
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)


print(ficha(n, g))
