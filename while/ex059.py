import time

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0

while opção != 5:

    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('Qual sua opção? '))

    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'O produto entre {n1} e {n2} é {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Informe novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção invalida, tente novamente ')
    print('=' * 30)
    time.sleep(2)

print('Fim do programa')
