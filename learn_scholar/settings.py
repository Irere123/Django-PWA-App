"""
Django settings for learn_scholar project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import socket

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h&1n=z^4#7=)h3dupdex=!gy!-xb3m2h#a-mm)$sl*_*m&6%b6'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG for deployment and production
DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # My Apps
    'journal',
    'community',
    'users',

    # 3rd Party Apps
    'bootstrap4',
    'social_django',
    'django_extensions',
    'friendship',
    'pwa',


    # Django default apps
    'django.contrib.sites', # new
    'django.contrib.sitemaps', # new
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1 # new

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

# New
REST_FRAMEWORK = {    
    'DEFAULT_PERMISSION_CLASSES': [      
        'rest_framework.permissions.jangoModelPermissionsOrAnonReadOnly'    
    ]
}

#add this # New
AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# New
SOCIAL_AUTH_FACEBOOK_KEY = '637266440171142'       # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8762149c9cbdd480b20bd59ed37584d0'  # App Secret

ROOT_URLCONF = 'learn_scholar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]

WSGI_APPLICATION = 'learn_scholar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Learn Scholar ORG',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5000',
        'PASSWORD': 'irere2045 emmy',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# My settings
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'journal:index'
LOGOUT_URL = 'users:logout'
LOGOUT_REDIRECT_URL = 'users:login'

# PWA Settings
PWA_APP_NAME = 'Learn Scholar'
PWA_APP_DESCRIPTION = "#Track #Ask #Connect"
PWA_APP_THEME_COLOR = ' #04c0d194'
PWA_APP_BACKGROUND_COLOR = '#04C1D1'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait-primary'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/72x72.png',
        'sizes': '72x72'
    },
    {
        'src': '/static/images/144x144.png',
        'sizes': '144x144'
    },
    {
        'src': '/static/images/152x152.png',
        'sizes': '152x152'
    },
    {
        'src': '/static/images/192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/384x384png',
        'sizes': '384x384'
    },
    {
        'src': '/static/images/512x512.png',
        'sizes': '512x512'
    },
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/144x144.png',
        'sizes': '144x144'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/512x512.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'learn_scholar', 'serviceworker.js')