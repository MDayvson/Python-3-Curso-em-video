a = float(input('Primeiro segmento '))
b = float(input('Segundo segmento '))
c = float(input('Terceiro segmento '))
if a < b + c and b < a + c and c < a + b:
    print('OS segmento acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('OS segmento NÃO PODEM FORMAR um triângulo')