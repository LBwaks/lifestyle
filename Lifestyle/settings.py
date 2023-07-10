"""
Django settings for Lovubi project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url
import sentry_sdk
from decouple import config
from django.conf import settings
from django.contrib.messages import constants as messages
from dotenv import load_dotenv
from logtail import LogtailHandler
from sentry_sdk.integrations.django import DjangoIntegration
from datetime import timedelta

import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG")
DEBUG = False
ALLOWED_HOSTS = [".railway.app", "lovubi.com","127.0.0.1","https://lovubi.com/"]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 'localhost',
#   '127.0.0.1',
#   '111.222.333.444',
#   'mywebsite.example'


# Application definition

INSTALLED_APPS = [
     'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    'django.contrib.sitemaps',
    "django.contrib.postgres",
    "django.contrib.humanize",
    'hijack.contrib.admin',
    # created app
    "Blog",
    "Accounts",
    "Pages",
    # installed app
    "ckeditor",
    "ckeditor_uploader",
    "taggit",
    "admin_honeypot",
    "django_extensions",
    "hitcount",
    "crispy_forms",
     'defender',
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django_social_share",
    "django_cleanup.apps.CleanupConfig",
    "phonenumber_field",
    "debug_toolbar",
    'hijack',
    'maintenance_mode',
    # 'imagekit' ,
     
]

MIDDLEWARE = [
   
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
     'defender.middleware.FailedLoginMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'hijack.middleware.HijackUserMiddleware',
    'django_auto_logout.middleware.auto_logout',
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
]

ROOT_URLCONF = "Lifestyle.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django_auto_logout.context_processors.auto_logout_client', #autologout
            ],
        },
    },
]

WSGI_APPLICATION = "Lifestyle.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# development db settings
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("NAME"),
#         "USER": os.getenv("USER"),
#         "PASSWORD": os.getenv("PASSWORD"),
#         "HOST": os.getenv("HOST"),
#         "PORT": os.getenv("PORT"),
#     }
# }
# production db settings
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
}
# SENDGRID_SANDBOX_MODE_IN_DEBUG = False

# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
RECIPIENT_ADDRESS = os.getenv("RECIPIENT_ADDRESS")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = os.getenv('SERVER_EMAIL')

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# static settings


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# hitcount settings
HITCOUNT_KEEP_HIT_ACTIVE = {"days": 37365}
# crispy form
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# ckeditor
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_RESTRICT_BY_DATE = True
CKEDITOR_THUMBNAIL_SIZE = (500, 500)
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_IMAGE_QUALITY = 80


CKEDITOR_CONFIGS = {
    "default": {
        'skin': 'moono',
        # 'skin': 'office2013',
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
         # 'filebrowserUploadUrl': '/your-file-upload-url/',
        # 'filebrowserUploadMethod': 'form',
        'filebrowserImageUploadAllowed': True,
        'filebrowserImageMaxSize': 5242880,  # 5MB in bytes
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "clipboard",
                "items": ["Cut", "Copy", "Paste", "-", "Undo", "Redo"],
            },
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Subscript",
                    "Superscript",
                    "-",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                ],
            },
            {
                "name": "insert",
                "items": ["Image", "Flash", "Table", "HorizontalRule", "SpecialChar"],
            },
            {
                "name": "links",
                "items": [
                    "Link",
                    "Unlink",
                ],
            },
            "/",
            {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize"]},
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        "height": 291,
        "width": "auto",
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        "tabSpaces": 4,
        "removeDialogTabs": "link:advanced;link:upload;link:target;image:advanced;image:Link",
        "extraPlugins": ",".join(
            [
                "uploadimage",  # the upload image feature
                # your extra plugins here
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
    }
}
# messages
MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
# allauth
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
SITE_ID = 2
LOGIN_REDIRECT_URL = "blogs"
LOGOUT_REDIRECT_URL = "blogs"


# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_SESSION_REMEMBER = None


# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         "APP": {
#             "client_id": os.getenv("client_id"),
#             "secret": os.getenv("secret"),
#             "key": "",
#         }
#     }
# }
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = settings.LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN =180
ACCOUNT_EMAIL_MAX_LENGT = 254
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_LOGOUT_REDIRECT_URL = settings.LOGOUT_REDIRECT_URL
ACCOUNT_PREVENT_ENUMERATION = False
ACCOUNT_RATE_LIMITS = {
    # Change password view (for users already logged in
    "change_password": "5/m",
    # Email management (e.g. add, remove, change primary
    "manage_email": "10/m",
    # Request a password reset, global rate limit per IP
    "reset_password": "20/m",
    # Rate limit measured per individual email address
    "reset_password_email": "5/m",
    # Password reset (the view the password reset email links to.
    "reset_password_from_key": "20/m",
    # Signups.
    "signup": "20/m",
    # NOTE: Login is already protected via `ACCOUNT_LOGIN_ATTEMPTS_LIMIT`
}
ACCOUNT_SESSION_REMEMBER = None
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SIGNUP_REDIRECT_URL = settings.LOGIN_REDIRECT_URL
ACCOUNT_USERNAME_BLACKLIST = ["admin"]
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_REQUIRED = True
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USER_MODEL_EMAIL_FIELD ="email"
SOCIALACCOUNT_ADAPTER = "Accounts.adapters.CustomSocialAccountAdapter"

# logging
LOGGING_CONFIG = None
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime:s} {name} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime:s} {name} {module} {filename} {lineno:d} {funcName} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "logtail": {
            "class": "logtail.LogtailHandler",
            "formatter": "verbose",
            "source_token": os.getenv("LOGTAIL_SOURCE_TOKEN"),
        },
        "warning_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/blog_warning.log",
            "mode": "a",
            "formatter": "verbose",
            "level": "WARNING",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
        "error_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/blog_error.log",
            "mode": "a",
            "formatter": "verbose",
            "level": "ERROR",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
        "debug_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/blog_debug.log",
            "mode": "a",
            "formatter": "verbose",
            "level": "DEBUG",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
        "info_handle": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/blog_info.log",
            "mode": "a",
            "encoding": "utf-8",
            "formatter": "verbose",
            "level": "INFO",
            "backupCount": 5,
            "maxBytes": 1024 * 1024 * 5,
        },
    },
    "loggers": {
        "django": {
            "handlers": [
                "console",
                "error_handler",
                # "debug_handler",
                "warning_handler",
                "logtail",
            ],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["error_handler", "warning_handler"],
            "level": "INFO",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["error_handler", "warning_handler"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.server": {
            "handlers": ["error_handler", "warning_handler"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
DEBUG_PROPAGATE_EXCEPTIONS = True

COMPRESS_ENABLED = os.getenv('COMPRESS_ENABLED', False)
# jazminn

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Lovubi Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Lovubi",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Lovubi",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/Lovubi1.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Lovubi",

    # Copyright on the footer
    "copyright": "Lovubi Ltd",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["auth.User", "blog.Blog"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Homepage", "url": "home", "new_window": True},#

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "Blog"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "blog","Taggit", "Pages", "Accounts"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "blog": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fa-regular fa-blog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        'blog.Blog':'fas fa-blog',
        "blog.Comment":"fas fa-comments",
        # "accounts.Profile":"fas fa-id-card",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    # "language_chooser": True,
}


# deployment
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# aws

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"

AWS_QUERYSTRING_AUTH = False
AWS_QUERYSTRING_EXPIRE= 8
# AWS_S3_OBJECT_PARAMETERS = {"Access-Control-Allow-Origin": "*"}

# AWS_S3_CUSTOM_DOMAIN = 'https://d2n7j1cvfar59p.cloudfront.net'
# AWS_CLOUDFRONT_KEY = os.getenv("AWS_CLOUDFRONT_KEY",None).encode('ascii')
# AWS_CLOUDFRONT_KEY_ID =os.getenv("AWS_CLOUDFRONT_KEY_ID",None)
# s3 static settings
# AWS_LOCATION = "static"

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR / "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# media settings
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR / "media")
CKEDITOR_UPLOAD_PATH = "ckeditor/uploads"



# after https is configured
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
 # #  allauth
USE_X_FORWARDED_HOST = True

SECURE_BROWSER_XSS_FILTER = True
# http sttrict transport security

SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "same-origin"

# SECURE SSL REDIRECT
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# autologout
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=10),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}

# # sentry
sentry_sdk.init(
    dsn="https://d5ae51a5355c403d85995fe7d3724224@o4504099387342848.ingest.sentry.io/4505028709974016",
    integrations=[
        DjangoIntegration(
            transaction_style="url",
            middleware_spans=True,
            signals_spans=False,
        ),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
    send_default_pii=True,
)

# maintance
# if True the maintenance-mode will be activated
MAINTENANCE_MODE = None
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = False
MAINTENANCE_MODE_TEMPLATE = "errors/503.html"



# <a href="https://www.freepik.com/free-photo/world-diabetes-day-sugar-wooden-bowl-dark-surface_10401423.htm#query=sugar&position=0&from_view=keyword&track=sph">Image by jcomp</a> on Freepik