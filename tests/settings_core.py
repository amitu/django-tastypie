from settings import *
INSTALLED_APPS.append('django.contrib.sessions')
INSTALLED_APPS.append('core')
INSTALLED_APPS.append('oauth_provider')

ROOT_URLCONF = 'core.tests.api_urls'
MEDIA_URL = 'http://localhost:8080/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'simple': {
            'level': 'ERROR',
            'class': 'core.utils.SimpleHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['simple'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

AUTH_APP = 'auth_app'
AUTH_USER_MODEL = 'auth_app.User'
INSTALLED_APPS.append(AUTH_APP)
