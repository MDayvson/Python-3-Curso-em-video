def notas(*n, sit=False):
    """
    -> função para analisar notas e situação de alunos.
    :param n: uma ou mais notas.
    :param sit: (opcional) informaa situação do aluno.
    :return: um dicionario com o total, a maior e a menor nota, e situação.
    """
    aluno = {}

    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n) / len(n)

    if sit:

        if aluno['média'] < 5:
            aluno['situação'] = 'RUIN'
        elif aluno['média'] < 7:
            aluno['situação'] = 'RAZOAVEL'
        else:
            aluno['situação'] = 'BOA'

    return aluno


resp = notas(5.5, 2, 10, sit=True)
print(resp)
help(notas)
