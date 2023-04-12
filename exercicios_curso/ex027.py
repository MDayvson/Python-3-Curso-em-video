nome = input('Digite o nome completo: ').strip().title()
n = nome.split()
print(f'O primeiro nome é {n[0]}')
print(f'O ultimo nome é {n[len(n) - 1]}')
