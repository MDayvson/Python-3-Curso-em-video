# Exercício Python 72: Crie um programa que tenha uma dupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'Dois', 'Tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'desesseis', 'desessete',
           'dezoito', 'desenove', 'vinte')
while True:
    numero = int(input('Didite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
print(extenso[numero])
