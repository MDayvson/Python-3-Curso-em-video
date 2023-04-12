nome = input('Digite o nome: ').strip()
print(nome.upper())
print(nome.lower())
print(f'O nome tem {len(nome) - nome.count(" ")} letras')
lista = nome.split()

print(f'o primeiro nome tem: {len(lista[0])} letras')

