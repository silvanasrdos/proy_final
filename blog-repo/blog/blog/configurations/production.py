from .base import *

DEBUG = False


#TODO: DEJAR SOLO DOMINIO, cambiar la base de datos para la produccion
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'production-domain.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        #en caso de POSTGRESQL
        #'ENGINE': 'django.db.backends.postgresql',   

        #en caso de mysql
        #'ENGINE': 'django.db.backends.mysql',

        #'NAME':os.getenv('DB_NAME'), #valor de la variable DB_NAME en .env
        #USER
        #PASSWD
        #HOST
        #PORT
    }
}

os.environ['DJANGO_PORT'] = '1952' #8080