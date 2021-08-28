"""
Django settings for movieaudi project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ayn70^rrcc-9-+ynj2g&zl&%w99apoi!0kcge#(ohjd%4@sb5y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites',
    'crispy_forms',
    'accounts',
    'ads',
    'applications',
    'payment',
    'criteria',
    'widget_tweaks',
    'django_filters',
    'allauth',  
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'datetimewidget',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movieaudi.urls'
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates"),os.path.join(BASE_DIR,"templates","account")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'movieaudi.wsgi.application'
SITE_ID = 1


CONTENT_TYPES = ['video']

MAX_UPLOAD_SIZE = "24000000"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
SOCIALACCOUNT_AUTO_SIGNUP = False

SOCIALACCOUNT_ADAPTER ='accounts.adapter.MySocialAccountAdapter'
ACCOUNT_ADAPTER='accounts.accountadater.NoNewUsersAccountAdapter'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'photomovie',
        'USER': 'postgres',
        'PASSWORD': 'kausar',
        'HOST': '172.28.224.1',
        'PORT': '5432'

    }
}


AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
    
]

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
AUTH_USER_MODEL='accounts.User'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kausarbhimani7@gmail.com'
EMAIL_HOST_PASSWORD = 'Babira13$'
CRISPY_TEMPLATE_PACK='bootstrap3'

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


