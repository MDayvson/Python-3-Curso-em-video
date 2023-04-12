print('Gerador de PA')
print('='*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
termo = a1
while cont <= 10:
    print(f'{termo} ➜ ', end='')
    termo += r
    cont += 1
print('FIM')
