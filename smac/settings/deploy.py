import os, environ

from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file


environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', '165.246.241.59', '158.247.202.164', '192.168.0.16']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
