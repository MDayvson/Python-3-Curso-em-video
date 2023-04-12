from ex115.lib.interface import*
from ex115.lib.arquivo import*
import time

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    CriarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar conteudo do arquivo
        LerArquivo(arq)
    elif resposta == 2:
        # novo cadastro
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('ERRO: Digite uma opção valida')
    time.sleep(2)


