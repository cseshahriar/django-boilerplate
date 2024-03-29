import os
from app.local_settings import (
    SECRET_KEY, TEMPLATES_DIR, STATICFILES_DIR, STATIC_DIR, MEDIA_DIR,
    DEBUG, ENABLE_HTTPS, ALLOWED_HOSTS, INTERNAL_IPS, DB_CONFIG,
)
from app.loggings import LOGGING
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY  # local_settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG  # local_settings.py

ALLOWED_HOSTS = ALLOWED_HOSTS  # local_settings.py

# HTTPS configuration
if ENABLE_HTTPS:  # local_settings
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# needed for debug toolbar
INTERNAL_IPS = INTERNAL_IPS  # local_settings.py

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# add 3rd party applications here
PLUGIN_APPS = [
    "debug_toolbar",
    "rest_framework",
    'rest_framework.authtoken',
    "corsheaders",
    "import_export",
]

# add project applications here
PROJECT_APPS = [
    'users.apps.UsersConfig',
]

# consolidate all installed applications here
INSTALLED_APPS = DJANGO_APPS + PLUGIN_APPS + PROJECT_APPS

SITE_ID = 1  # Sites framework

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': os.getenv('DB_CONFIG', DB_CONFIG)
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) --------------------------------------
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR  # production, don't forget to run collectstatic
STATICFILES_DIRS = [
    STATICFILES_DIR,
]  # development environment

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_URL = 'manage'  # do not include any leading/trailing slashes

# Logging ---------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/logging/

LOGGING = LOGGING  # app/logging.py

# CORS HEADERS
# CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS
# CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allows from all origins when DEBUG mode on
CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = 'users.User'
APP_NAME = 'APP NAME'
