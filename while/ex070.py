print('-'*30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-'*30)

totpreço = totmaior1000 = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$ '))
    cont += 1

    totpreço += preço

    if preço > 1000:
        totmaior1000 += 1

    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print(f'{"FIM DO PROGRAMA":-^30}')
print(f'O total da compra foi de R$ {totpreço:.2f}')
print(f'Temos {totmaior1000} produto custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
