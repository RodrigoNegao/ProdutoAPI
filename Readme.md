## **Projeto de uso de Modelo E-COMMERCE Django REST API** :snake:

### O que contém o Projeto:
- Campo de filtragem;
- Personalização de alertas no sites (Testes de Respostas Django e Bootstrap);
- Testes de CRUD personalizados;
- Teste de bancos de dados salvos no SQLite;
- Uploads de Fotos;
- Compactação das fotos para otimização do Servidor;
- Uso de API DRF com autentificação por Login e Token;

## Para uma boa instalação e testes siga a ordem abaixo.

### Ambiente Django no Windows

[Configurar Ambiente (Env) no Python](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

### Criar Ambiente com Conda/Anaconda
- Instale o ANACONDA 
- Primeiro Configure cmd [Configurar Ambiente(Env) Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- Digite: 
```bash
activate base
```
- Crie um AMBIENTE no cmd: 
```bash
conda create -n ECAPI python
```
- Ative o AMBIENTE:
```bash
 activate ECAPI
 ```
- Instale os Requisitos:
```bash
 pip install -r requirements.txt
 ```
## Config Django para Migração - siga o ordem por causa da FK Categoria/Produto(caso crie um banco de dados NOVO)
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py migrate category
python manage.py makemigrations category
python manage.py migrate category
python manage.py migrate product
python manage.py makemigrations product
python manage.py migrate product
python manage.py migrate authtoken
python manage.py createsuperuser
```
- Cadastro de Categoria somente no [ADMIN](http://127.0.0.1:8000/admin/)

[Link API](http://127.0.0.1:8000/api/)
-http://127.0.0.1:8000/api/

- Criar Token para Usuario:
```bash
 python manage.py drf_create_token NOMEDOUSUARIO
 ```
 - Link para Gerar Token tem mandar login
 http://127.0.0.1:8000/api-token-auth/ usename=  password=

 [Gerando Token DRF](https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens)

- Login: admin
- Senha: admin
