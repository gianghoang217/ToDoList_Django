import os
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'github_actions'),  # Default for CI
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),  # 'localhost' for GitHub Actions, 'postgres' for CircleCI
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

# Optional: Debugging log to confirm settings during CI runs
if os.environ.get('DEBUG_SETTINGS', 'false').lower() == 'true':
    print("Database settings for testing:")
    print(f"ENGINE: {DATABASES['default']['ENGINE']}")
    print(f"NAME: {DATABASES['default']['NAME']}")
    print(f"USER: {DATABASES['default']['USER']}")
    print(f"PASSWORD: {DATABASES['default']['PASSWORD']}")
    print(f"HOST: {DATABASES['default']['HOST']}")
    print(f"PORT: {DATABASES['default']['PORT']}")