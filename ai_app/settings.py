"""
Django settings for ai_app project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
from socket import gethostname
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&02n-2@66o#w+h-92gd(da-*zc5bgp7l-l5g1siq1p5)aosu&c'

# SECURITY WARNING: don't run with debug turned on in production!
"""
DEBUG = False
try:
    from .local_settings import *
except ImportError:
    pass
"""
"""
ALLOWED_HOSTS = [
    'ec2-52-91-179-24.compute-1.amazonaws.com',
]
"""
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'predictions.apps.PredictionsConfig',
    'bootstrap4'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Heroku用追加
]

ROOT_URLCONF = 'ai_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_predict',  # DB name
        'USER': 'root',
        "HOST": "127.0.0.1",
        "PORT": "3306",
        'OPTIONS': {
            # 'read_default_file': '/path/to/my.cnf',
            'init_command': 'SET default_storage_engine=INNODB',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
"""
#db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

"""
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
"""
LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 管理サイトのログイン機能を通常のログイン機能として使う
#LOGIN_URL = 'admin:login'

LOGIN_URL = 'predictions:login'
# ログイン後トップページにリダイレクト
LOGIN_REDIRECT_URL = 'predictions:predict'
# ログアウト後はログインページに
LOGOUT_REDIRECT_URL = 'predictions:top'

# Eメール用
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# メールサーバーへの接続設定
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sa1361ku@gmail.com'
EMAIL_HOST_PASSWORD = 'uniidxjifhiunmlp'
EMAIL_USE_TLS = True

# コマンドライン出力用
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'predictions/static')

hostname = gethostname()
if "ip-172-31-37-195.ec2.internal" in hostname:  # ローカル の場合
    DEBUG = True  # ローカルでDebug
    #import pymysql
    #pymysql.install_as_MySQLdb()
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',  # DB name
            'USER': 'root',
            'PASSWORD':'@Pass0601',
            "HOST": 'localhost',
            "PORT": '3306',
            'OPTIONS': {
                # 'read_default_file': '/path/to/my.cnf',
                'init_command': 'SET default_storage_engine=INNODB',
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
    ALLOWED_HOSTS = [
        'ec2-52-91-179-24.compute-1.amazonaws.com',
    ]
else:
     # 本番環境
    DEBUG = True
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            },
        },
    }

    # DB設定
    import dj_database_url
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    db_from_env = dj_database_url.config()
    DATABASES = {
        'default': dj_database_url.config()
    }
    ALLOWED_HOSTS = [
        'ec2-52-91-179-24.compute-1.amazonaws.com',

    ]