print(f'{" LOJA ":=^40}')
preço = float(input('Preço das compras: R$ '))
condição = int(input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual opção? '''))

if condição == 1:
    print(f'Sua compra de R$ {preço} vai custar {preço - preço * 0.1:.2f}')
elif condição == 2:
    print(f'Sua compra de R$ {preço} vai custar R$ {preço - preço * 0.05:.2f}')
elif condição == 3:
    print(f' Sua compra de R$ {preço} será parcelada em 2x de R$ {preço / 2:.2f} ')
elif condição == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}X de R$ {(preço + preço * 0.2) / parcelas:.2f} com juros')
    print(f'Sua compra de R$ {preço} vai custar R$ {preço + preço * 0.2:.2f} ')
else:
    print('OPÇÃO INVALIDA')