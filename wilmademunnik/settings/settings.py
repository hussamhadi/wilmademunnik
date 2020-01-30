import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = False

ADMINS = (
    ('Hussam Hadi', 'info@empowermen.nl'),
)
MANAGERS = ADMINS


DEFAULT_FROM_EMAIL   = 'django-admin@wilmademunnik.nl'
SERVER_EMAIL         = DEFAULT_FROM_EMAIL
EMAIL_HOST           = 'in-v3.mailjet.com'
EMAIL_PORT           = 587
EMAIL_HOST_USER      = '****'
EMAIL_HOST_PASSWORD  = '****'
EMAIL_SUBJECT_PREFIX = '[Django] wilmademunnik.nl '

LANGUAGES = [('nl', 'Nederlands'),]
DEFAULT_LANGUAGE = 0


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': 'wilmademunnik_dev.sqlite',
        # 'USER': 'empowermen',
        # 'PASSWORD': 'hellercopter',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wilma_new_prod',
        'USER': '****',
        'PASSWORD': '****',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'nl'
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'pasf^2y=hy^e=0vr@haymra73nj2-+^4qhcq(i%&amp;03y_2v-tl0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'wilmademunnik.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wilmademunnik.wsgi.application'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'cms.context_processors.cms_settings',
            'sekizai.context_processors.sekizai',
        ],
    },

}]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.redirects',
    'debug_toolbar',
    'rosetta',
    'sorl.thumbnail',
    'sekizai',

    'filebrowser',
    'mptt',
    'filer',
    'easy_thumbnails',
    'cms',
    'djangocms_text_ckeditor',
    'djangocms_picture',

    'menus',
    'contact',
    'project',
    'treebeard',
    'wilmademunnik',
    'captcha',
)

RECAPTCHA_PUBLIC_KEY = '6LfTz6AUAAAAABeBGGQe2SKl6havNUocAdsxMOfR'
RECAPTCHA_PRIVATE_KEY = '6LfTz6AUAAAAACLz4DbXd3TPJSpV4pfgYRgMaHOr'

CMS_SEO_FIELDS = True
CMS_TEMPLATES = (
    ('base.html', 'Main Template'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/var/log/django.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

