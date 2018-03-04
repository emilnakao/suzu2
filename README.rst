# Desenvolvendo

## Branch nova: django11

`workon django11`

## Migrações de banco

```
python manage.py migrate
```

```

```


# Para rodar pela primeira vez:

- Execute na pasta raiz do projeto o comando `docker-compose up`

- Crie um superusuário:

1) verifique o id do container docker usando o comando `docker ps`

2) abra o shell nesse container:

`docker exec -i -t <id> /bin/bash`

3) rode o comando `suzu/manage.py createsuperuser --settings=suzu.settings.docker`