n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está em REPROVADO')
elif 5 < media < 7:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
