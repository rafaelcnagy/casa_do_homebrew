# Casa do homebrew

Um site para compartilhamento de conteúdo autoral de RPG.

# Instruções
O que você precisa fazer para rodar o projeto

## Pré Requisitos
Ter instalado em seu computador:
```
- Python 3.7
- MySQL
```

## Como instalar
Siga o passo a passo:

-   Execute o comando no terminal do **MySQL**:
    ```
    CREATE DATABASE 'db_casadohomebrew'@'localhost';
    ```

- No arquivo ```/casa_do_homebrew/settings.py```, próximo da linha 85, inserir credenciais do banco de dados em:
   
    ```
    'USER': 'django',
    'PASSWORD': 'django',
    ``` 

-    Execute os comandos no terminal:
    
    ```
    pip install pipenv
    pipenv install
    pipenv run python manage.py migrate
    ```

## Como rodar
Execute o comando no terminal:
```
pipenv run python manage.py runserver 
```