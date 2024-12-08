from .base import *
from decouple import config

DEBUG = False
ADMINS = [
 ('KYD', 'kydallaboutlearning@gmail.com'),
]
ALLOWED_HOSTS = ['*']



#addin the postgres db
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': config('POSTGRES_DB'),
 'USER': config('POSTGRES_USER'),
 'PASSWORD': config('POSTGRES_PASSWORD'),
 'HOST': 'db',
 'PORT': 5432,
 }
}