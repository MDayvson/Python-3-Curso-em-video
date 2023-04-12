import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print(f'O site não está acessivel no momento.')
else:
    print(f'Consegui acessar o site com sucesso')


#chat gpt
"""import requests

url = 'https://www.google.com/'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'O site {url} está acessível.')
    else:
        print(f'O site {url} está indisponível.')
except requests.exceptions.RequestException as e:
    print(f'O site {url} está indisponível. O erro foi: {e}')
"""

# atravez de uma def
"""def verificar_site(url):
    import requests

    url = f'https://{url}/'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'O site {url} está acessível.')
        else:
            print(f'O site {url} está indisponível.')
    except requests.exceptions.RequestException as e:
        print(f'O site {url} está indisponível. O erro foi: {e}')


site = str(input('SITE: '))
verificar_site(site)
"""