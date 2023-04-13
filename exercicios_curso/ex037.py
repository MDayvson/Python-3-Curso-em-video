num = int(input('Digite um número inteiro: '))
base = int(input('''Escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL 
Sua escolha: '''))
if base == 1:
    resultado = bin(num)
elif base == 2:
    resultado = oct(num)
elif base == 3:
    resultado = hex(num)
else:
    print('Escolha uma base valida')
print(f'{num} convertido é igual a {resultado[2:]} ')
