"""
Django settings for jazminleon project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

os.environ.setdefault('DJANGO_SECRET_KEY', "prvESVBoA7x81xdMqvRRYuofHfvUDXYa+iU2RRC9P2g")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
print(SECRET_KEY)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SITE_ID = 1

DEBUG = True

# Application definition
INSTALLED_APPS = [
    'collectfast',
   # This project

    'website',
    'blog',
    'contact',
    'documents_gallery',
    'events',
    'gallery',
    'pages',
    'people',
    'products',
    'utils',

    'gunicorn',

    'storages',
    'django_redis',
    'anymail',

    # CodeRed CMS
    'coderedcms',
    'bootstrap4',
    'compressor',
    'modelcluster',
    'taggit',
    'wagtailfontawesome',
    'wagtailcache',
    'wagtailimportexport',
    'wagtail_feeds',

    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.routable_page',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.search_promotions',
    #'wagtail.contrib.postgres_search',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.core',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
    'wagtail.admin',
    'wagtailmarkdown',

    'fluentcms_cookielaw',
    'fluentcms_countdown',

    'wagalytics',
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'wagtail.contrib.frontend_cache',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    # Save pages to cache. Must be FIRST.
    'wagtailcache.cache.UpdateCacheMiddleware',

    # Common functionality
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Security
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Error reporting. Uncomment this to recieve emails when a 404 is triggered.
    'django.middleware.common.BrokenLinkEmailsMiddleware',

    # CMS functionality
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

    # Fetch from cache. Must be LAST.
    'wagtailcache.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'jazminleon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
                'django.template.context_processors.request',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
        },
    },
]

WSGI_APPLICATION = 'jazminleon.wsgi.application'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'BACKEND': 'django.db.backends.mysql',
        'NAME': "jazleonLLC_db",
        'USER': "joanne&jazmin",
        'PASSWORD': "!jo&jaz0802!",
        'HOST': "localhost",
	'LOCATION': "/opt/bitnami/mysql/tmp/mysql.sock",
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB; SET sql_mode="STRICT_TRANS_TABLES";',
        }
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ],
    },
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': "redis://mURvj06YNtaEO1GqGLOGJfeDgUMDOS3k@redis-13687.c60.us-west-1-2.ec2.cloud.redislabs.com:13687/0",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        },
    }
}

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = 'jazminleon.users.adapters.AccountAdapter'
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = 'jazminleon.users.adapters.SocialAccountAdapter'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Jazmin Leon]'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = "AKIA225UXCKHHOZSFCRK"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_SECRET_ACCESS_KEY = "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"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_STORAGE_BUCKET_NAME = "jazminleonmindset"
AWS_CONTENT_BUCKET_NAME = "jazminleoncontent"
AWS_MEDIA_CONTAINER = "ncfc5lqohmarsq"
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_QUERYSTRING_AUTH = False
# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': f'max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate',
}

AWS_DEFAULT_ACL = 'authenticated-read'
AWS_S3_ENCRYPTION = True
AWS_S3_FILE_OVERWRITE = False

# STATIC
# ------------------------
STATICFILES_STORAGE = 'config.settings.production.StaticRootS3Boto3Storage'
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# MEDIA
# ------------------------------------------------------------------------------
# region http://stackoverflow.com/questions/10390244/
# Full-fledge class: https://stackoverflow.com/a/18046120/104731
from storages.backends.s3boto3 import S3Boto3Storage  # noqa E402
# import datetime

class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = STATIC_URL + 'static/'


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = STATIC_URL + 'media/'

# endregion
DEFAULT_FILE_STORAGE = 'config.settings.production.MediaRootS3Boto3Storage'

date_format = "%a, %b %d %Y %H:%M:%S"

# exp_date = datetime.datetime.today() + datetime.timedelta(weeks=1)

# Login
LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'


# Wagtail settings
WAGTAIL_SITE_NAME = "Jazmin Leon LLC"
WAGTAIL_ENABLE_UPDATE_CHECK = False

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://www.burnout-coaching.jazminleon.com'


# Bootstrap
BOOTSTRAP4 = {
    # set to blank since coderedcms already loads jquery and bootstrap
    'jquery_url': '',
    'base_url': '',
    # remove green highlight on inputs
    'success_css_class': ''
}


# Tags
TAGGIT_CASE_INSENSITIVE = True

EMAIL_SUBJECT_PREFIX = '[Jazmin Leon]'


# Anymail (Mailgun)
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
EMAIL_BACKENDS = {
    'mailgun': 'anymail.backends.mailgun.EmailBackend',
    'sendgrid': 'anymail.backends.sendgrid.EmailBackend',
}
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
ANYMAIL = {
    'MAILGUN_API_KEY': "ac31b978d55db1ad145de209d4bdce97-7bce17e5-b98f0545",
    'MAILGUN_SENDER_DOMAIN': "mg.jazminleon",
    'SENDGRID_API_KEY': "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",
}

COMPRESS_ENABLED = True
COMPRESS_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_CACHEABLE_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_OFFLINE = True
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_URL
COMPRESS_URL = STATIC_URL # noqa F405# Collectfast
# ------------------------------------------------------------------------------
# https://github.com/antonagestam/collectfast#installation
AWS_PRELOAD_METADATA = True


BITNAMI_PASSWORD = "riw30vRaOznP"
ALLOWED_HOSTS = ["burnout-coaching.jazminleon.com", "www.burnout-coaching.jazminleon.com", "34.211.57.30"]

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

DJANGO_ADMIN_USER = "jazminleon"
EMAIL_HOST_USER = "jazmin@jazminleon.com"
DJANGO_ADMIN_PASSWD = "!jazminleonLLC0802!"
EMAIL_HOST_PASSWORD = "!JLmsc&sLLC0802!"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.google.com'
EMAIL_HOST_USER = DJANGO_ADMIN_EMAIL
EMAIL_HOST_PASSWORD = DJANGO_EMAIL_PASSWORD
EMAIL_PORT = 587

WEB_CONCURRENCY = 10

SENDWITHUS_API_KEY="live_ed8da937a1ae6e46e3d5382aa35b9c52dc323128"

# Storage
# AWS
CLOUDFRONT_ID="E2HLBGEI70XI0I"
CLOUDFRONT_DOMAIN="d345v9s5k3vk6a.cloudfront.net"
AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN

# Databases
REDIS_CACHE2_URL="redis://rlAYAXJFLUVjVOOEkSGezuoR5a3Y4IwV@redis-11862.c16.us-east-1-2.ec2.cloud.redislabs.com:11862/0"

# Google Analytics
GA_VIEW_ID="ga:194610369"
GA_KEY_CONTENT='{"type": "service_account", "project_id": "jazmin-leon-llc", "private_key_id": "07d0287395d5a1cfbe49adb646906da46eb37a8a", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCtMUBCag+kcSy9\n8F1Covo7wEHl/KQC+Mz/Qdh8oz8fKBC9fKxKMD7vnLe8JutOC8NElF4WPH4ysmJp\n/8cUo9Kcj8hMZoQs6ebMw+++6zELFek0ZRgwondIoCgKs1HBTvnnsFTUmNmdnWiH\noC13/jouuyekWB5kKSE0YMW9BmxA/dMWQ2aZVzicvyIxrnH1h/MZYQrPPCbZ2lEe\n4Q/EIOV9Pu7qPxj+lAmNQeWcNTTYnKyJR9JElEjAkdpxwyjW5Xv+OKyv50qjHeFB\n1EonMzpHNb+T3F5jl46rz2+egoTL1yFqV8iLznmJDJ8ehsNqXDUCjattyEWhEFlJ\nphagYilpAgMBAAECggEAJ2bHyYRDHERyKyEaun0FBGB0LYxJTPLJAn56r7pc8yvk\niRNqx/MLcmxbQZcyG76h1UGS2Si4hjSenqJl6oxtrxgn97ev9N7e1vFxouPzc6Pv\nuu+P7gqcLB3hljOfEyUyRhNP7VD72zeTLx3SElU4a+bAuUsh2OQhjX7BpcQnDy6/\nF6e1hb2rdtPEWBH1hWA/+BD3iRRPZhBdmzuhKKiaDmITJEtOPdgM/HnzQn8ie8Pa\n1oywOCIYy6tXQX2grij03qKNl416F7S6kKCZVrKw9pSvPeLgllbkuddEkCBQ5VVV\noDZ8PMqOg/iRTLXi06fxNtEhloaYgW+RrsfYb7b+zQKBgQDyqbj2WV8U1E/MCR+y\nAYbMAlLzkfoyO7fBaOxykoy/14LYulH+cGYBCX2Qm9hkLU052RRBsENkV3XJQNm3\nBgJBHLqQr61HRbMDW65h0f6akwgwqB+HcKCvMEkl8OqD9XeSw1pnEk5q0w6tv7e5\noT90sOzYdaKmmtJ6FLKWJuTapQKBgQC2thMYdNUUV8h1ajTCqzh7NpSIwf0Ma/fo\nggQ/yLiz2XCZNHbZZr+NO91NPLm0e2rgESNqhD+AEakeqNVRhdxvOekkoZsjC28T\nzn5eKk5NlXDwyvMVlwp63vxsVDRlRUUp1FRX3hgTPBaIwNMbW7wmonMvA81d8xvX\n4LpJq9iMdQKBgDV4cppN/SaQ1fiGtiY6MeK4TGEBdJknEYmbviZM5pjLOzjYbYLc\nb42g8rsvrBH+7XpmvBDxbxgoMXskQBUVTN/eHboOC+edkyGVTSqe5DRZW7+k/DWS\n+sU/pY6ntHVZXHzJcR0vKnpdgWmFyk0sG9hxt+7GlQ2TJffioat2bI1FAoGAEmcq\nazcxUxg4Z6Mn50epq7dmpJOtcjfZw4B8/xOvjuXi0nuXUPRpbMdP1fy807HupNz1\nDUB+yN5+g0kMG2b5OfbCRd9FKfV33a3ZypBGTMg1lPtMGquY8aFOGXctw9mDSuBJ\nEoSbNizCNEn/uWy2+ck5As5GPCVFc6v993eomxUCgYEAsZOE7azpvgt8G+zI9lhc\n3Im7agzlR7ZdelZbQt9l/TcDbXzvcl/XzV+9LV5m2VsrniBnnPO/O0Q4LHEmgPba\nwlPZc4fDUSNNyKaEyFe+XMzlMoEzOizWui5W7JAkWgvuD05TGw2eMSXihUlB+N0l\n0+Ug+GZ4RGdMVls7hHvNHhg=\n-----END PRIVATE KEY-----\n", "client_email": "wagalytics@jazmin-leon-llc.iam.gserviceaccount.com", "client_id": "115316613644768253856", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/wagalytics%40jazmin-leon-llc.iam.gserviceaccount.com"}'