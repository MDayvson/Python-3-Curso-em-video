pilha = []
exp = str(input('Digite a expressão: '))
for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão está errada')

