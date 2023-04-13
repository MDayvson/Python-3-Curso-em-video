def aumentar(preço, taxa):
    """
    -> Aumenta o preço a uma determinada taxa.
    :param preço: valor a ser aumentado.
    :param taxa: taxa de aumento.
    :return: o valor aumentado.
    """
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    """
    -> Diminui o preço a uma determinada taxa.
    :param preço: valor a ser diminuido.
    :param taxa: taxa de diminuição.
    :return: o valor diminuido.
    """
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    """
    -> dobra um valor.
    :param preço: valor a ser dobrado
    :return: o dobro do preço.
    """
    res = preço * 2
    return res


def metade(preço):
    """
    -> reduz um valor a metade.
    :param preço: valor a ser reduzido a metade.
    :return: a metade do valor.
    """
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
