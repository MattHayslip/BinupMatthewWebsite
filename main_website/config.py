import os
from pathlib import Path  # Python 3.6 + only
from dotenv import load_dotenv, find_dotenv  # for using dotenv

load_dotenv(find_dotenv())

class Config(object):
    DEBUG                           = True  # auto reloading the app
    TESTING                         = False
    CSRF_ENABLED                    = True
    SQLALCHEMY_TRACK_MODIFICATIONS  = True
    apphost                         = os.getenv("HOST")  # where it's being hosted
    port                            = os.getenv("PORT")  # which port is being hosted on

    db_unique = True

    # cookie handling the HTTPS and other security
    SESSION_COOKIE_SECURE   = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'

    # mailing
    MAIL_SERVER    = 'smtp.gmail.com'
    MAIL_PORT      = 465
    MAIL_USE_TLS   = False
    MAIL_USE_SSL   = True
    MAIL_USERNAME  = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD  = os.getenv("MAIL_PASSWORD")

    # db
    db_ip          = os.getenv("ip")
    db_name        = os.getenv("db")
    db_username    = os.getenv("username")
    db_password    = os.getenv("password")


class ProductionConfig(Config):
    DEBUG                           = False
    SECRET_KEY                      = os.getenv("secret_key_production")
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    Threaded                        = True 


class DevelopmentConfig(Config):
    ENV                             = "Development"
    DEVELOPMENT                     = True
    SECRET_KEY                      = os.getenv("secret_key_dev")
    OAUTHLIB_INSECURE_TRANSPORT     = True
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

