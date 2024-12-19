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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

