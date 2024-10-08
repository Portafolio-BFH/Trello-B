from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'Trello_B',
        'HOST': 'localhost',
        'PORT': 1433,
        'USER': 'sa',
        'PASSWORD': '72130870aA',
        'TRUSTED_CONNECTION': 'no'
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'