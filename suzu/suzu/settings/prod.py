# The following environment variables are required to deploy in production:
# SECRET_KEY
# DJANGO_SETTINGS_MODULE : set to suzu.settings.prod
# DB_PASSWORD
# DB_NAME
# DB_USER

from base import *
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable("SECRET_KEY")
DB_PASSWORD = get_env_variable("DB_PASSWORD")
DB_NAME = get_env_variable("DB_NAME")
DB_USER = get_env_variable("DB_USER")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': '',
        'PORT': '3306',
    }
}