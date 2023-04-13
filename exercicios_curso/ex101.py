def voto(nasc):
    """
    => verifica idade e analisa a situação do voto.
    :param nasc: Ano de nascimento
    :return: a situação se o voto é obrigatorio ou opcional
    """
    import datetime
    hoje = datetime.datetime.today().year
    idade = hoje - nasc

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    if idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPICIONAL'
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


ano = int(input('Em que ano voçê nasceu? '))
print(f'{voto(ano)}')
help(voto)
