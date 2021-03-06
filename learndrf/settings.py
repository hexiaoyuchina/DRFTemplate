"""
Django settings for learndrf project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8t3x#jz_uko0r0qba!ceyqmvqha74$of%g4a1m+v&xnn4c$pd='

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
    'rest_framework',
    'api'
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

ROOT_URLCONF = 'learndrf.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'learndrf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spider',
        'HOST': "localhost",
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': 3306,
        'CHARSET': 'UTF-8'

    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

LOG_DIR = './logs/'

LOOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # ??????????????????????????????
    'formatters': {
        # ?????????????????????????????????????????????????????????????????????????????????????????????????????????
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(pathname)s %(lineno)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(filename)s[line:%(lineno)d %(funcName)s] - %(levelname)s: %(message)s'
        },
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(request_id)s] [%(name)s::%(lineno)d] >>>>>>>func: %(funcName)s : %(message)s'
        },
    },
    'filter': {
        'require_debug_true': {
            '()': 'django.utils.logs.RequireDebugTrue',
        },
        'request_id': {  # ?????????????????????????????????????????????????????????
            '()': 'utils.logs.filter.RequestIDFilter'
        }
    },
    # ???????????????
    'handlers': {
        'console': {
            'level': 'DEBUG',  # ????????????
            'filters': ['request_id'],  # ?????????
            'class': 'logging.StreamHandler',  # ?????????
            'formatter': 'standard',  # ?????????????????????
        },
        'default': {
            'level': 'DEBUG',
            'calss': 'utils.logs.MyLoggerHandler',
            'filters': ['request_id'],
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'when': 'MONTH',  # ????????????????????????????????????
            'backupCount': 365,
            'formatter': 'standard'
        },
        'info': {
                    'level': 'DEBUG',
                    'calss': 'utils.logs.MyLoggerHandler',
                    'filters': ['request_id'],
                    'filename': os.path.join(LOG_DIR, 'debug.log'),
                    'when': 'MONTH',  # ????????????????????????????????????
                    'backupCount': 365,
                    'formatter': 'standard'
                },
    },
    # ?????????????????????????????????????????????????????????
    'loggers': {
        '': {
          'handlers': ['console'],
          'level': 'DEBUG'
        },
        'douban': {
            'handlers': ['info'],
            'level': 'DEBUG',
            'propagate': False,
        }

    }

}