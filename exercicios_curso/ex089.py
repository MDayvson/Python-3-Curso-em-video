classe = []

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1 + nota2 / 2)
    classe.append([nome, [nota1, nota2], media])

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ')
        if resp == 'N':
            break
    if resp == 'N':
        break

print('='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('='*30)

for i, a in enumerate(classe):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('='*30)
    opção = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if opção == 999:
        print('FiNALIZANDO...')
        break
    if opção <= len(classe) - 1:
        print(f'Notas de {classe[opção][0]} são {classe[opção][1]}')
print('Volte sempre')
