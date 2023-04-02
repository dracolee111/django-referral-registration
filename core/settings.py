import os
from pathlib import Path
from dotenv import load_dotenv

# DIRS
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(BASE_DIR.joinpath('.env'))
TEMPLATE_DIR = os.path.join(CORE_DIR, "templates") 
WSGI_APPLICATION = 'core.wsgi.application'

### VARIABLES
SECRET_KEY = os.getenv('SECRET_KEY', default='$EKR!T_Ce?')
DEBUG = os.getenv('DEBUG', default=True)
ALLOWED_HOSTS = os.getenv('HOSTS', default=['*'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'main',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

#### WSGI
WSGI_APPLICATION = 'core.wsgi.application'


######### DATABASES
if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
            'USER': 'admin',
            'PASSWORD': 'pa$$word',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT"),
        }
    }


#### AUTHENTICATION
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
LOGIN_REDIRECT_URL = 'profile.html'
LOGOUT_REDIRECT_URL = 'login'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


######### STATIC
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'static'),
)
SITE_NAME = os.getenv("SITE_NAME")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_COOKIE_AGE	= 86400 #2 days

### EMAILS
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend' ## use '...backends.smtp.EmailBackend' to send real emails after defining the variables in .env
EMAIL_FILE_PATH = os.path.join(CORE_DIR, 'sent_emails')
EMAIL_HOST = os.getenv('EMAIL_HOST', default='127.0.0.1')
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", default='user')
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", default='pa$$word')
EMAIL_PORT = os.getenv("EMAIL_PORT", default='5432')

