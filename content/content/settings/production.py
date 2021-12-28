from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-psl!00xzg02o3_wlp!^5vq2b4_g-1y987qdzh(-l$+7#r(y&$a'

ALLOWED_HOSTS = ['quran-contents.com', 'www.quran-contents.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
