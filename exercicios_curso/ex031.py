dist = float(input('Qual a distancia da sua viagem? '))
print(f'Voçê está prestes a começar uma viagem de {dist} KM.')
if dist <= 200:
    preço=dist*0.5
else:
    preço=dist*0.45
print(f'E o preço da sua passagem será de R$ {preço:.2f}')

