from .base import *
from decouple import config

DEBUG = True

ADMINS = [
    ('KYD', 'kydallaboutlearning@gmail.com'),
]
ALLOWED_HOSTS = ['*']

# Database Configuration
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT')
    }
}

