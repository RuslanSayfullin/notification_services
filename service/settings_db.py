from service.psw import dbase_psw

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'service',
        'USER': 'portaluser',
        'PASSWORD': dbase_psw,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}