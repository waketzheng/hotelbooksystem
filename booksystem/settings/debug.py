from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# django debug toolbar
# https://github.com/jazzband/django-debug-toolbar

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": "//cdn.bootcss.com/jquery/2.1.4/jquery.min.js",
    "SHOW_TOOLBAR_CALLBACK": lambda x: True,
    "SHOW_COLLAPSED": True,
}
