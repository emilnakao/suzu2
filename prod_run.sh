#!/bin/bash

./suzu/manage.py syncdb --settings=suzu.settings.docker
./suzu/manage.py migrate --all --settings=suzu.settings.docker
./suzu/manage.py initdb --settings=suzu.settings.docker
./suzu/manage.py runserver 0.0.0.0:8000 --settings=suzu.settings.docker
# uwsgi --ini uwsgi.ini