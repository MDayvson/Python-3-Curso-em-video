import random
cont = 1
computador = random.randint(0, 10)

n = int(input('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Séra que voçe consegue advinhar qual foi?
qual o seu palpite? '''))
while n != computador:
    cont += 1
    if n > computador:
        print('Menos...', end='')
    else:
        print('Mais...', end='')
    n = int(input('Tente mais uma vez. '))
print(f'Acertou com {cont} tentativas')
