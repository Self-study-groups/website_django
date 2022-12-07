from .base import *

DEBUG = True

# Database Config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override Installer Apps

INSTALLED_APPS +=[

]