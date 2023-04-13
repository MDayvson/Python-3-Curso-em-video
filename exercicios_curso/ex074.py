import random

n = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
     random.randint(0, 10), random.randint(0, 10),)

for c in n:
    print(c, end=' ')
print('')
print(f'o maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')

