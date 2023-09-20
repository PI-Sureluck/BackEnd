# SureLuck - Aproveite Suas Apostas com Segurança

O SureLuck é um projeto que visa criar uma plataforma de SureBets especializada em apostas em esportes eletrônicos (E-Sport), permitindo aos usuários identificar oportunidades de apostas onde é possível garantir lucro, independentemente do resultado da partida. A estratégia se baseia no cálculo de probabilidades de diferentes casas de apostas, e nosso sistema automatizado tornará esse processo simples e eficiente.

## Tecnologias Utilizadas

### Backend:
- **Python com Django:** O backend do SureLuck é desenvolvido utilizando Python com o framework Django, proporcionando uma base sólida para a lógica de negócios e interação com o banco de dados mysql.

### Front-end:
- **Vue.js:** O frontend do SureLuck é construído utilizando Vue.js, permitindo uma interface de usuário dinâmica e responsiva para os usuários interagirem com as funcionalidades do site.

## Equipe

- **José Renan ([GitHub](https://github.com/thisisrenan))**: Desenvolvedor Back-End.
- **Caio Rangel ([GitHub](https://github.com/caio741))**: Desenvolvedor Back-End.
- **ingrid ([GitHub](https://github.com/ingridrsm))**: Desenvolvedor Front-End.
- **Evandro ([GitHub](https://github.com/Evandrogv123))**: Desenvolvedor Front-End.

## Como Instalar


## Endpoints da API

A API do SureLuck oferece diversos endpoints que permitem interagir com a plataforma, obter informações sobre as apostas, e muito mais. Abaixo estão os principais endpoints e suas funcionalidades:

## Sites EndPoints

--- 
### `GET /sites/site/`  retorna todos os sites

Este endpoint retorna informações sobre todos os sites específicos na plataforma.

#### Requisição
- Método: GET
  - Endpoint: `/sites/site/`

#### Exemplo de Resposta
```json
{
  {
    "id": 1,
    "name": "site",
    "link": "site.com.br",
    "logo": "",
    "xpath": ""
  }
  {
    "id": 2,
    "name": "site2",
    "link": "site2.com.br",
    "logo": "",
    "xpath": ""
  }
}

```
---

### `GET /sites/site/id`  retorna apenas um site

Este endpoint retorna informações sobre um site específico na plataforma.

#### Requisição
- Método: GET
  - Endpoint: `/sites/site/id`

#### Exemplo de Resposta
```json
{
  "id": 1,
  "name": "site",
  "link": "site.com.br",
  "logo": "",
  "xpath": ""
}

```
---

### `POST /sites/site/` Cadastra um site

Este endpoint cadastra um site na plataforma.

#### Requisição
- Método: POST
  - Endpoint: `/sites/site/`

#### Parâmetros esperados 
```json
{
  "name": "site",
  "link": "site.com.br",
  "logo": "",
  "xpath": ""
}
```
---

### `PUT /sites/site/id` Edita um site

Este endpoint edita um site específico na plataforma.

#### Requisição
- Método: PUT
  - Endpoint: `/sites/site/id`

#### Parâmetros esperados 
```json
{
  "name": "site",
  "link": "site.com.br",
  "logo": "",
  "xpath": ""
}
```
OBS: caso queira alterar apenas um item pode passar os outros com o parâmetro vazio 

---

### `DELETE /sites/site/id` Deleta um site

Este endpoint deleta um site específico na plataforma.

#### Requisição
- Método: DELETE
  - Endpoint: `/sites/site/id`

---


## Users EndPoints

--- 
### `GET /users/user/`  retorna todos os usuários

Este endpoint retorna informações sobre todos os usuários específicos na plataforma.

#### Requisição
- Método: GET
  - Endpoint: `/users/user/`

#### Exemplo de Resposta
```json
{
    {
      "id": 123,
      "username": "teste123",
      "email": "teste123@example.com"
    }
    {
      "id": 123,
      "username": "teste123",
      "email": "teste123@example.com"
    }
}

```
---

### `GET /users/user/id`  retorna apenas um usuário

Este endpoint retorna informações sobre um usuário específico na plataforma.

#### Requisição
- Método: GET
  - Endpoint: `/users/user/id`

#### Exemplo de Resposta
```json

{
  "id": 123,
  "username": "teste123",
  "email": "teste123@example.com"
}


```
---

### `POST /users/user/` Cadastra um usuário

Este endpoint cadastra o usuário na plataforma.

#### Requisição
- Método: POST
  - Endpoint: `/users/user/`

#### Parâmetros esperados 
```json
{
  "username": "teste123",
  "email": "teste123@example.com",
  "password": "senha"
}
```
---

### `PUT /users/user/id` Edita um usuário

Este endpoint edita um usuário específico na plataforma.

#### Requisição
- Método: PUT
  - Endpoint: `/users/user/id`

#### Parâmetros esperados 
```json
{
  "username": "teste123",
  "email": "teste123@example.com"
  "password": "senha"
}
```
OBS: caso queira alterar apenas um item pode passar os outros com o parâmetro vazio 

---

### `DELETE /users/user/id` Deleta um usuário

Este endpoint deleta um usuário específico na plataforma.

#### Requisição
- Método: DELETE
  - Endpoint: `/users/user/id`

---


## Events EndPoints

--- 
### `GET /sites/event/`  retorna todos os eventos

Este endpoint retorna informações sobre todos os eventos específicos na plataforma.

#### Requisição
- Método: GET
  - Endpoint: `/sites/event/`

#### Exemplo de Resposta
```json
{
	"status": 200,
	"message": "Events encontrados",
	"events": [
		{
			"id": 3,
			"name": "teste152f0",
			"date": "2023-09-20",
			"teamA": "timeAaa",
			"teamB": "timebbbb"
		},
		{
			"id": 4,
			"name": "eventofoda",
			"date": "2023-10-20",
			"teamA": "timeAaa",
			"teamB": "timebbbb"
		}
	]
}

```
---

### `GET /sites/event/id`  retorna apenas um evento

Este endpoint retorna informações sobre um evento específico na plataforma.

#### Requisição
- Método: GET
  - Endpoint: `/sites/event/id`

#### Exemplo de Resposta
```json
{
	"status": 200,
	"message": "Event encontrado",
	"event": [
		{
			"id": 3,
			"name": "teste152f0",
			"date": "2023-09-20",
			"teamA": "timeAaa",
			"teamB": "timebbbb"
		}
	]
}
```
---

### `POST /sites/event/` Cadastra um evento

Este endpoint cadastra um evento na plataforma.

#### Requisição
- Método: POST
  - Endpoint: `/sites/event/`

#### Parâmetros esperados 
```json
{
  "name":"eventofoda",
  "date":"2023-12-20",
  "teamA":"timeAaa",
  "teamB":"timebbbb"
}
```
---

### `PUT /sites/event/id` Edita um evento

Este endpoint edita um evento específico na plataforma.

#### Requisição
- Método: PUT
  - Endpoint: `/sites/event/id`

#### Parâmetros esperados 
```json
{
  "name":"eventofoda",
  "date":"2023-12-20",
  "teamA":"timeAaa",
  "teamB":"timebbbb"
}
```
OBS: caso queira alterar apenas um item pode passar os outros com o parâmetro vazio 

---

### `DELETE /sites/event/id` Deleta um evento

Este endpoint deleta um evento específico na plataforma.

#### Requisição
- Método: DELETE
  - Endpoint: `/sites/event/id`

---


## Aviso Legal

O SureLuck é um site que oferece informações e oportunidades de apostas em esportes eletrônicos (E-Sport). No entanto, é fundamental compreender que apostas envolvem riscos e, como tal, não podemos garantir lucro ou ausência de perdas.

O usuário reconhece que:

- Todas as apostas feitas são de sua própria responsabilidade.
- O SureLuck não se responsabiliza por quaisquer perdas financeiras ou danos causados por apostas feitas com base nas informações fornecidas pelo site.
- As informações disponíveis no SureLuck são para fins informativos e educacionais, e não constituem aconselhamento financeiro ou recomendação de apostas.

É responsabilidade do usuário analisar as informações disponíveis, avaliar os riscos e tomar decisões informadas antes de realizar qualquer aposta. Recomendamos apostar com responsabilidade e dentro dos limites do seu orçamento.


## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
