import requests

cep = '88150000'
url = 'https://viacep.com.br/ws/{}/json'.format(cep)

response = requests.get(url)
endereco = response.json()
print(endereco)
print(type(endereco))
print(endereco['localidade'])
