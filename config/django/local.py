from config.django.base import *

# pymysql.install_as_MySQLdb()

# requirements DB setting
# Then in Local, use sqlite3
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": env("MYSQL_DATABASE", default="survey_gather"),
#         "USER": env("MYSQL_USER", default="root"),
#         "PASSWORD": env("MYSQL_PASSWORD", default="password"),
#         "HOST": env("MYSQL_HOST", default="localhost"),
#         "PORT": env("MYSQL_PORT", default="3306"),
#         "OPTIONS": env.dict("MYSQL_OPTIONS", default={}),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SESSION_COOKIE_SECURE = True
