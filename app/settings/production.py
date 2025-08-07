from .base import *



host = config('HOST_PRODUCTION')
ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PGDATABASE'),
        'USER': config('PGUSER'),
        'PASSWORD': config('PGPASSWORD'),
        'HOST': config('PGHOST'),
        'PORT': config('PGPORT'),
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = '/static/'
STATIC_ROOT = "staticfiles"  



# configuracion de archivos aws produccion  

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

# Configuración de almacenamiento estático en AWS S3
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

#STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Configuración de almacenamiento de archivos de medios en AWS S3
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
PUBLIC_MEDIA_LOCATION = 'media_cdn'

DEFAULT_FILE_STORAGE = 'app.storage_settigns.MediaStorage'  

# Configuración adicional opcional
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"



import sentry_sdk

sentry_sdk.init(
    dsn=config('DNS'),
    send_default_pii=True,
    traces_sample_rate=1.0,
    _experiments={
        "continuous_profiling_auto_start": True,
    },
)