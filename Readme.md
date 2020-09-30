## **Projeto de uso de Modelo E-COMMERCE Django REST API** :snake:

- Login: admin
- Senha: admin

## Para uma boa instalação e testes siga a ordem abaixo.

### Ambiente Django no Windows

[Configurar Ambiente (Env) no Python](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

### Criar Ambiente com Conda
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
- Criar Token para Usuario:
```bash
 python manage.py drf_create_token NOMEDOUSUARIO
 ```
 - Usuario Link Gerar Token
 http://127.0.0.1:8000/api-token-auth/

## Config Django caso crie um banco de dados NOVO
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py migrate product
python manage.py makemigrations product
python manage.py migrate product
python manage.py migrate authtoken
python manage.py createsuperuser
```
