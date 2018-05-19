import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "if4s&rsp65^oe*o!%%e*(%x9*pxazr0&bae%+&50a*cer$a(xa"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True and "romanload" not in BASE_DIR

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "backend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "booksystem.urls"

WSGI_APPLICATION = "booksystem.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
if not DEBUG:
    from .local_settings import email_conf, qiniu_conf, DATABASES

    # qiniu settigs for upload used by 'qiniuyun.QiniuPush'
    # https://github.com/qiniu/python-sdk
    QINIU_CONF = qiniu_conf

    #  Email ,ref:http://www.cnblogs.com/BeginMan/p/3443158.html
    globals().update(email_conf)

    # some settings
    ALLOWED_HOSTS = ["127.0.0.1"]
    INSTALLED_APPS.append("qiniuyun")
else:
    # django debug toolbar
    # https://github.com/jazzband/django-debug-toolbar
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1", "0.0.0.0"]
    DEBUG_TOOLBAR_CONFIG = {
        "JQUERY_URL": "//cdn.bootcss.com/jquery/2.1.4/jquery.min.js",
        "SHOW_TOOLBAR_CALLBACK": lambda x: True,
        "SHOW_COLLAPSED": True,
    }

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
