print(f'{" SEQUENCIA DE FIBONACCI ":.^40}')
n = int(input('Quantos números voçê quer mostrar? '))
cont = 3
t1 = 0
t2 = 1

print(f'{t1} ➜ {t2} ➜ ', end='')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} ➜ ', end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')
