# Spotnews

Bem-vindo ao repositório do Spotnews! Este é um projeto desenvolvido como parte do curso da Trybe, que consiste em um site de notícias construído com Django.

## Descrição do Projeto

O Spotnews é uma aplicação web que permite aos usuários visualizar e categorizar notícias. Ele oferece funcionalidades como criar, visualizar e editar notícias, além de categorizá-las.

## Como Executar o Projeto

Siga estas instruções para executar o projeto em seu ambiente local:

### Pré-requisitos

- Python 3.x instalado em seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/).
- Docker instalado e configurado em seu sistema. Você pode encontrar instruções de instalação [aqui](https://docs.docker.com/get-docker/).

### Passos

1. Clone este repositório em seu ambiente local:

git clone git@github.com:ronaldocipriiano/spotnews.git

2. Navegue até o diretório do projeto:

cd spotnews

3. Execute o MySQL via Docker com o seguinte comando:

docker build -t spotnews-db .
docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db

4. Crie um ambiente virtual e ative-o:

python3 -m venv .venv
source .venv/bin/activate

5. Instale as dependências do projeto:

pip install -r requirements.txt

6. Execute as migrações do banco de dados:

python3 manage.py migrate

7. Execute o script para popular o banco de dados:

python3 manage.py runscript seeds

8. Inicie o servidor:

python3 manage.py runserver

9. Acesse o projeto em seu navegador utilizando o seguinte endereço:

http://127.0.0.1:8000/

## Tecnologias Utilizadas

- Django
- Django Rest Framework
- MySQL
- HTML
- CSS

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue caso encontre algum problema ou para propor melhorias.
