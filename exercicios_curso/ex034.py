salario = float(input('Qual o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + salario * 0.15
else:
    novo = salario + salario * 0.1
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {novo:.2f} agora.')
