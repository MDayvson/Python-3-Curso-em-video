peso = float(input('Qual o seu peso? (KG) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura ** 2
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('PARABENS, voçê está no peso ideal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está em obesidade')
else:
    print('Você está em obesidade Morbida')