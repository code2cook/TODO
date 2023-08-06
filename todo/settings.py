

from pathlib import Path

from storages.backends.s3boto3 import S3Boto3Storage
import boto3
import json

import base64
from botocore.exceptions import ClientError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'storages',
  
    
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

CSRF_COOKIE_DOMAIN = 'myblogs.click'
CSRF_TRUSTED_ORIGINS = ['https://myblogs.click']



ROOT_URLCONF = 'todo.urls'

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

WSGI_APPLICATION = 'todo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATICFILES_DIRS = [BASE_DIR /'app/static/']



# AWS_S3_REGION_NAME = 'us-east-1' 
# # Initialize AWS Secrets Manager client
# secrets_manager_client = boto3.client('secretsmanager',region_name = AWS_S3_REGION_NAME )

# # Function to retrieve the secret value from AWS Secrets Manager
# def get_secret_value(secret_name):
#     response = secrets_manager_client.get_secret_value(SecretId=secret_name)
#     if 'SecretString' in response:
#         return json.loads(response['SecretString'])
#     raise ValueError('Secret value not found')

# secrets = get_secret_value('MyDjangoAppSecrets')

# AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']

# SECRET_KEY = secrets['SECRET_KEY']
# # AWS settings
# AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
#  # e.g., 'us-east-1'



def get_secret(secret_name, region_name):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        # Get the secret value
        response = client.get_secret_value(SecretId=secret_name)

        # Decrypt the secret value if necessary
        if 'SecretString' in response:
            secret = response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(response['SecretBinary'])
            secret = decoded_binary_secret.decode('utf-8')

        return secret
    except ClientError as e:
        # Error handling code here
        pass
    
secret_name = "MyDjangoAppSecrets"
region_name = "us-east-1"

secret_value= get_secret(secret_name, region_name)

secrets= json.loads(secret_value)




SECRET_KEY = secrets.get('SECRET_KEY')
# AWS settings
AWS_ACCESS_KEY_ID = secrets.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = secrets.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = secrets.get('AWS_STORAGE_BUCKET_NAME')


# SECRET_KEY = '4dq_8o)0)**l=9n(#@u^d9*akz07l0-i)q&9h#vj4=-a7r)_87'
# AWS_ACCESS_KEY_ID = 'AKIASMG7BS4EEVWRMGXV'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME ='myblog-s3-storage'

# For serving static files directly from S3
STATIC_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# For serving media files (user-uploaded files) from S3
# MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

