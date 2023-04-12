def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Aumenta o preço a uma determinada taxa.
    :param formato: (opcional) formatar como moeda.
    :param preço: valor a ser aumentado.
    :param taxa: taxa de aumento.
    :return: o valor aumentado.
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Diminui o preço a uma determinada taxa.
    :param formato: (opcional) formatar como moeda.
    :param preço: valor a ser diminuido.
    :param taxa: taxa de diminuição.
    :return: o valor diminuido.
    """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    -> dobra um valor.
    :param formato: (opcional) formatar como moeda.
    :param preço: valor a ser dobrado
    :return: o dobro do preço.
    """
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    -> reduz um valor a metade.
    :param formato: (opcional) formatar como moeda.
    :param preço: valor a ser reduzido a metade.
    :return: a metade do valor.
    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% redução: \t{diminuir(preço, taxar, True)} ')
    print('-'*30)
