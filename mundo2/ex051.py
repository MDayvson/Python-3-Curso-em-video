a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r
for c in range(a1, decimo+1, r):
    print(f'{c}', end=' ')


