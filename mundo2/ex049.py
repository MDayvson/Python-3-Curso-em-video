n = int(input('Digite um número para ver a tabuada: '))
print(f'{f" TABUADA DE {n} ":=^20}')
for c in range(1, 11):
    print(f'{n:2} x {c:2} = {n*c:2}')
print('='*20)
