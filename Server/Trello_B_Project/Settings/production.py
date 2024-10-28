from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'Trello_B',
        'HOST': 'localhost',
        'PORT': 1433,
        'USER': 'sa',
        'PASSWORD': '72130870aA',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'TrustServerCertificate': 'yes',
        }
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'