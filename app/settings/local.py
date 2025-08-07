from .base import *


ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# configuracion de archivos static y media
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = '/static/'
STATIC_ROOT = "staticfiles"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')