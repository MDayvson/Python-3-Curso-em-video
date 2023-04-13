print(f'{" GERADOR DE PA ":-^30}')
a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
cont = 1
termo = a1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ➜ ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostrar a mais: '))
print('FIM')
print(f'Foram mostrados {total} termos')
