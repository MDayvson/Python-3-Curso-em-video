cont = 0
soma = 0

n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print(f'Voçê digitou {cont} números e a soma entre eles foi de {soma}')
