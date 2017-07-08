# FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild
# CMD [ "hello.wsgi" ]

# Start with a Python image.
FROM python:2.7-onbuild

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Install some necessary things.
RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

# Django settings module
RUN export DJANGO_SETTINGS_MODULE=suzu.suzu.settings.dev

# Collect our static media.
RUN /code/suzu/manage.py collectstatic --noinput --settings=suzu.settings.dev

# Specify the command to run when the image is run.
CMD ["/code/prod_run.sh"]