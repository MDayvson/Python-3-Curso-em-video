import random
import time

num = random.randint(0, 5)
print('=' * 50)
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('=' * 50)
n = int(input('Em que número pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if n == num:
    print('PARABENS! Voçê consegui me vencer! ')
else:
    print(f'GANHEI! eu pensei no número {num} e não no {n}! ')
