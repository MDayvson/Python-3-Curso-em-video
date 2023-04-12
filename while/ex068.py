import random
cont = 0
while True:

    computador = random.randint(0, 10)
    jogador = int(input('Diga um valor: '))
    if (computador + jogador) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    opção = ' '
    while opção not in 'PI':
        opção = input('Par ou Impar? [P/I] ').strip().upper()[0]

    print(f'Voçê jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador} deu {resultado}')

    if opção == resultado[0]:
        cont += 1
        print('Voçê venceu')
        print('Vamos jogar novamente')
    else:
        break
print('Voçê PERDEU!')
print('='*30)
print(f'GAME OVER! Você venceu {cont} vezes')
