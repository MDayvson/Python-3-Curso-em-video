vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('Multado! Voçê excedeu o limite permitido que é de 80km/h')
    print(f'Voçê deve pagar uma multa de R$ {(vel - 80) * 7:.2f}!')
print('Tenha um bom dia e dirija com segurança! ')
