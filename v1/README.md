# Request 

Esse estudo tem como objetivo estudar requisições HTTP e consumos de API utilizando Python.

A ideia do desenvolvimento é consumir a API do GitHub para que possamos passar um usuário e termos o retorno de algumas iformações do perfil da pessoa.

## Como fazer ? 

* Inicialmente precisaremos utilizar a Biblioteca "Request" para fazer as requisições.
```
pip install requests

import requests
```

<br/>

* Precisamos criar um input para receber o preenchimento do consumidor e adicionar na url de consumo pré estabelecido.

```
username = input("Digite seu nome de usuário: ")
url = f'https://api.github.com/users/{username}'
```

* Precisamos fazer a requisição e armazenar seu response em uma variavel, e após armazenar, precisamos converter para JSON.

```
response = requests.get(url)
data = response.json()
```

<br/>

* Criamos uma condicional para devolver o response quando a requisição der tudo certo, e o que fazer quando der erro na requisição.
```
if response.status_code == 200:
    #print(data)
    print(f'Nome completo: {data["name"]}')
    print(f'Localização: {data["location"]}')
else: 
    print('Não foi possivel encontrar o usuário')
```
