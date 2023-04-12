media = cont = soma = maior = menor = 0

resp = 'S'

while resp == 'S':
    n = int(input('Digite um número: '))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Voçê digitou {cont} números e a média foi de {soma / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
