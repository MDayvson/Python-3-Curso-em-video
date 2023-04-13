aluno = {}
classe = []

while True:

    aluno['Nome'] = str(input('Nome: ')).title().strip()
    aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: ').strip())

    if aluno['Média'] < 5:
        aluno['Situação'] = 'REPROVADO'
    elif 5 >= aluno['Média'] < 7:
        aluno['Situação'] = 'RECUPERAÇÂO'
    elif aluno['Média'] >= 7:
        aluno['Situação'] = 'APROVADO'

    classe.append(aluno.copy())
    aluno.clear()

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break

print('-=' * 30)

for aluno in classe:

    for k, v in aluno.items():
        print(f'- {k} é igual a {v}')
    print('-='*30)
