jogador = {}
gols = []
time = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    gols.clear()

    for cont in range(1, tot + 1):
        gols.append(int(input(f'    Quantos gols na partida {cont}? ')))

    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)

    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)

print('cod', end=' ')      # cabeçalho
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-= ' * 30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()

print('-=' * 30)

while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe o jogador com código {busca}')
    else:
        print(f'--- Levantamento do Jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-='*30)
print('FIM')
