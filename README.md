# Casa do homebrew

Um site para compartilhamento de conteúdo autoral de RPG.

# Instruções
O que você precisa fazer para rodar o projeto

## Pré Requisitos
Ter instalado em seu computador:
```
- Python 3.8
- poetry
- MySQL
```

## Como instalar
Siga o passo a passo:

-   Execute o comando no terminal do **MySQL**:
    ```
    CREATE DATABASE db_casadohomebrew;
    ```

-   No arquivo ```/casa_do_homebrew/settings.py```, próximo da linha 85, inserir credenciais do banco de dados em:
   
    ```
    'USER': 'django',
    'PASSWORD': 'django',
    ``` 


-   Instale o ambiente virtual:
    
    ```
    poetry install
    ```
    
> Se ocorrer erros ao instalar o mysqlclient, instale os pacotes abaixo e tente novamente:
>
>`sudo apt-get install default-libmysqlclient-dev build-essential`

-   Prepare o banco de dados
    ```
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
    ```
  
## Como rodar
Execute o comando no terminal:
```
poetry run python manage.py runserver 
```

---

## TO DO LIST

- [x] Enviar arquivos
- [x] Login
- [x] Limitações ao enviar arquivo
- [x] Update arquivo-user
- [ ] CRUD arquivos
- [ ] Votos
- [ ] CustomUser