from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's35@$4=t9$l98j^8xne7vby01jajixwnc6)xk*3-%4n@a(fbk3'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'settings/db.sqlite3'),
    }
}