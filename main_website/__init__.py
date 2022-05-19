from flask              import Flask
from flask_wtf.csrf     import CSRFProtect
from flask_sqlalchemy   import SQLAlchemy
from os                 import path

# import os
# from flask_login import LoginManager

from .lib.util import error

from .config import Config, DevelopmentConfig, ProductionConfig

APP     = Flask(__name__)
DB      = SQLAlchemy()
DB_NAME = "my_temp_db"
TEMP_DB = f'sqlite:///{DB_NAME}.db'  # temporary db for testing

# the mysql connection
MYSQL_DB_CONN = f'mysql+pymysql://{Config.db_username}:{Config.db_password}@{Config.db_ip}/{Config.db_name}'

# xcsrf 
csrf = CSRFProtect()

def run_app():
    try:
        APP.config['SECRET_KEY'] = DevelopmentConfig.SECRET_KEY
        APP.config['SQLALCHEMY_DATABASE_URI']        = TEMP_DB # replace with MYSQL_DB_CONN to use outside mysql db
        APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS

        # mail
        APP.config['MAIL_SERVER']   = Config.MAIL_SERVER
        APP.config['MAIL_PORT']     = Config.MAIL_PORT
        APP.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
        APP.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
        APP.config['MAIL_USE_TLS']  = Config.MAIL_USE_TLS
        APP.config['MAIL_USE_SSL']  = Config.MAIL_USE_SSL

        # starting the database
        DB.init_app(APP)

        # cross site request forgery protection
        csrf.init_app(APP)

        # registering the views and api controllers
        # to use api or different files / scripts use the bottom 2 code
        from .views import views

        APP.register_blueprint(views, url_prefix='/')

        # from .models import UserContact, NewsLetter

        create_database(APP)

        # region not sure why this it's needed but it's needed
        # login_manager = LoginManager()
        # login_manager.login_view = 'admin.login'  # handling the login
        # login_manager.init_app(app)

        # @login_manager.user_loader
        # def load_user(id):
        #     return UserContact.query.get(int(id))

        # @login_manager.user_loader
        # def load_user(id):
        #     return NewsLetter.query.get(int(id))

        # @login_manager.user_loader
        # def load_user(id):
        #     return admin.query.get(int(id))

        # endregion

        return APP

    except Exception as e:
        print(f'{error} * error in __init__: <-- {str(e)}')


def create_database(APP):
    if not path.exists('website/' + DB_NAME):
        DB.create_all(app=APP)
        print(f' * Created Database!')
