frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(f'o inverso de {junto} é {inverso}')

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindomo')
else:
    print('Não temos um palindromo')
