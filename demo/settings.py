# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from shards.config import sharded_config
# import sharding

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p5(l-obrk3c7^y_snfdm2mlyt(r&b)f^1py3evh9_*0^)zjjiw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoApp'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'todoApp/templates')],
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

WSGI_APPLICATION = 'demo.wsgi.application'

DATABASE_ROUTERS = ['shards.routers.ShardedRouter']

SHARDING = sharded_config({
    'unsharded': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'todo',
            'USER': 'scalica',
            'PASSWORD': 'scalica123',
            'HOST': 'mysql5.csoh7r1rzta2.us-west-2.rds.amazonaws.com',
            'PORT': '3306'
        },
    },
    'sharded': {
        'shard_group_one': {
            'logical_shards': 1024,
            'db1': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'todo',
                'USER': 'scalica',
                'PASSWORD': 'scalica123',
                'HOST': 'mysql7.csoh7r1rzta2.us-west-2.rds.amazonaws.com',
                'PORT': '3306'
            },
            'db2': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'todo',
                'USER': 'scalica',
                'PASSWORD': 'scalica123',
                'HOST': 'mysql8.csoh7r1rzta2.us-west-2.rds.amazonaws.com',
                'PORT': '3306'
            },
        }
    }
})

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = SHARDING.db_config

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo',
        'USER': 'scalica',
        'PASSWORD': 'scalica123',
        'HOST': 'mysql5.csoh7r1rzta2.us-west-2.rds.amazonaws.com',
        'PORT': '3306'
    }
}
'''
# OTHER DATABASES ON AMAZON
# mysql6.csoh7r1rzta2.us-west-2.rds.amazonaws.com
# mysql7.csoh7r1rzta2.us-west-2.rds.amazonaws.com
# mysql8.csoh7r1rzta2.us-west-2.rds.amazonaws.com
# username (for all): scalica
# password (for all): scalica123
# port (for all): 3306

# DATABASE_ROUTERS = ['sharding.routers.ShardedRouter']
#
# SHARDING = sharded_config({
#     'unsharded': {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         },
#     },
#     'sharded': {
#         'shard_group_one': {
#             'logical_shards': 1024,
#             'db1': {
#                 'ENGINE': 'django.db.backends.sqlite3',
#                 'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
#             },
#             'db2': {
#                 'ENGINE': 'django.db.backends.sqlite3',
#                 'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
#             }
#         }
#     }
# })

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
