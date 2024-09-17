# Api Cliente (Customer) - Projeto MVP

Projeto MVP para disciplina **Desenvolvimento Full Stack Básico** 

Este projeto é uma aplicação back-end desenvolvida com Python Utilizando Flask. O objetivo é criar um serviço para interagir com front-end permitindo adicionar, editar, excluir e visualizar informações dos clientes.


## Funcionalidades

- **Cadastro de Clientes**: Permite adicionar novos clientes com informações como nome, email, telefone, idade e endereço.
- **Alteração de Clientes**: Permite alterar as informações dos clientes existentes.
- **Busca de Clientes**: Permite buscar as informações dos clientes existentes para edição.
- **Exclusão de Clientes**: Permite excluir clientes do banco de dados.
- **Visualização de Clientes**: Lista todos os clientes cadastrados com opções para editar e excluir.
- **Busca de Cep: Permite Consultar os dados de endereço, informando o CEP.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no projeto.
- **Flask**: Framework para desenvolvimento da API.
- **SQLite**: Banco de dados utilizado para armazenar os dados dos clientes e endereços.
- **Pydantic**: Biblioteca para validação de dados e definição de esquemas.
- **flask-openapi3**: Biblioteca para documentação da API.

## Como executar 

Será necessário ter o python instalado. A versão indicada é a 3.12.6 e a do pip é a 24.2
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Instale o venv:

```
 python -m venv .venv 
```

Ative o Venv com o comando abaixo:

```
 .venv\Scripts\activate
```

Assim que ativado, instale as depedencias.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

## Documentação OpenAPI

A documentação OpenAPI da API está disponível em:

- **URL**: `[http://localhost:5000/openapi/swagger](http://localhost:5000/openapi/swagger)`


## POSTMAN

Para executar, importe as collections do postman 

```
customer-api.postman_collection.json
```

## Autor
Clayton Morais de Oliveira
