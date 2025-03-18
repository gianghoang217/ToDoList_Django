import os
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'github_actions'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}