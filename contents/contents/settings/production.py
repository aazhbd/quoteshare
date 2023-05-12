from .base import *

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DEBUG = False

SECRET_KEY = 'rhbrzudcp7q=o5$@55r&j1c1-f+z5h$z6s60h@^ulxms(=6a5a'

ALLOWED_HOSTS = ['quran-contents.com', 'www.quran-contents.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
