from .base import *
from .local import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "prvESVBoA7x81xdMqvRRYuofHfvUDXYa+iU2RRC9P2g"

COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

INSTALLED_APPS += [
    'wagtail.contrib.frontend_cache',
    'gunicorn',
]
INSTALLED_APPS = ['collectfast'] + INSTALLED_APPS

# Add your site's domain name(s) here.
ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS

# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/2.1/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = 'Jazmin Leon LLC <noreply@jazminleon.com>'

# A list of people who get error notifications.
ADMINS = [
    ('Jazmin Leon', 'jazmin@jazminleon.com'),
    ('Joanne Jordan', 'joanne.k.m.jordan@gmail.com')
]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'HOST': 'localhost',
#        'NAME': 'jazminleon',
#        'USER': 'jazminleon',
#        'PASSWORD': '',
#        # If using SSL to connect to a cloud mysql database, spedify the CA as so.
#        'OPTIONS': { 'ssl': { 'ca': '/path/to/certificate-authority.pem' } },
#    }
#}

# Use template caching to speed up wagtail admin and front-end.
# Requires reloading web server to pick up template changes.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.google.com'
EMAIL_HOST_USER = DJANGO_ADMIN_EMAIL
EMAIL_HOST_PASSWORD = DJANGO_EMAIL_PASSWORD
EMAIL_PORT = 587

WEB_CONCURRENCY = 10
