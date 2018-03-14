from .base import *
import dj_database_url
import os

DEBUG = False

ALLOWED_HOSTS = ["dogger-app.herokuapp.com"] # aquí va el dominio que le pondremos a heroku

SECRET_KEY = os.getenv("SECRET_KEY", None)

DATABASES = dict()

DATABASES["default"] = dj_database_url.config(conn_max_age=500)
