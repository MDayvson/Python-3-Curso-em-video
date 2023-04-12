num = int(input('Digite um número: '))

print(f'Analisando o número {num}')
print(f'Unidades {num//1%10}')
print(f'Dezenas {num//10%10}')
print(f'Centenas {num//100%10}')
print(f'Milhar {num//1000%10}')
