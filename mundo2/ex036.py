valor = float(input('Valor da casa: R$ '))
salario = float(input('Sálario do comprador: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
prestação = valor / (tempo*12)
if prestação > salario*0.3:
    print(f'Emprestimo NEGADO')
else:
    print(f'Para pagar uma casa de R$ {valor} em {tempo} anos a prestação será de R$ {prestação:.2f} ')