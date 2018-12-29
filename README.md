# SUZU 2 [![Build Status](https://travis-ci.org/emilnakao/suzu2.svg?branch=master)](https://travis-ci.org/emilnakao/suzu2)

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

## Gerando arquivos de fixture para testes

1. Subir a aplicação e popular o banco
2. Rodar o comando `suzu/manage.py dumpdata`. Exemplo:

```
suzu/manage.py dumpdata --format=json --settings=suzu.settings.dev_emil --natural-foreign auth > suzu/attendancebook/fixtures/auth.json
suzu/manage.py dumpdata --format=json --settings=suzu.settings.dev_emil --natural-foreign attendancebook > suzu/attendancebook/fixtures/attendancebook.json
```

A opção `--natural-foreign` gera referências a chaves naturais de alguns registros, como `content-type`, ao invés de depender de pks que podem variar de execução a execução.