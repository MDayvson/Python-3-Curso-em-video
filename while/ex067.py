print(f'{"TABUADA":-^30}')
while True:
    cont = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='*30)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n:2} x {cont:2} = {n*cont:2}')
        cont += 1
    print('='*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
