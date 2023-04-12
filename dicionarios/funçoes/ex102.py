def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: o valor do fatorial de um número num.
    """
    fat = 1
    for cont in range(num, 0, -1):
        fat *= cont
        if show == True:
            print(f'{cont}', end=' ')
            if cont > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return fat


print(fatorial(5, show=True))
