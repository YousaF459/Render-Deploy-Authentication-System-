import os
import dj_database_url
from .settings import * 
from .settings import BASE_DIR


#ALLOWED_HOSTS=[os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
ALLOWED_HOSTS = [
    os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'render-deploy-authentication-system.onrender.com'),
    'localhost', '127.0.0.1'
]
#CSRF_TRUSTED_ORIGINS=['https://'+ os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

CSRF_TRUSTED_ORIGINS = [
    'https://render-deploy-authentication-system.onrender.com',
    'https://render-deploy-authentication-system-react.onrender.com'
]


DEBUG=False
SECRET_KEY=os.environ.get('SECRET_KEY')


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    "https://render-deploy-authentication-system-react.onrender.com",
]
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_EXPOSE_HEADERS = ['Set-Cookie']




STORAGES={
    "default" : {
        "BACKEND":"django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedStaticFilesStorage", 
    }
}


DATABASES={
    'default':dj_database_url.config(
        default=os.environ['DATABASE_URL'],
        conn_max_age=600,

    )
}

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY') 
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

SENDGRID_SANDBOX_MODE_IN_DEBUG = False 