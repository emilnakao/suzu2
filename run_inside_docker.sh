#!/bin/bash

./suzu/manage.py migrate --settings=suzu.settings.docker
./suzu/manage.py runserver 0.0.0.0:8000 --settings=suzu.settings.docker