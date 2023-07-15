import requests

username = input("Digite seu nome de usuário: ")
url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    #print(data)
    print(f'Nome completo: {data["name"]}')
    print(f'Localização: {data["location"]}')
else: 
    print('Não foi possivel encontrar o usuário')
