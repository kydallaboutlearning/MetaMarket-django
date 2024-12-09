from .base import *
from decouple import config

DEBUG = False

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
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Setting up cache
REDIS_URL = 'redis://cache:6379'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_URL,
    }
}

# Setting up channel layers
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}
