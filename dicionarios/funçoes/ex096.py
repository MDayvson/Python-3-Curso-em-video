def area(largura, comprimento):
    print(f'A area de um terreno de {largura} x {comprimento} é de {largura * comprimento}m².')


print('CONTROLE DE TERRENOS')
print('-='*10)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
