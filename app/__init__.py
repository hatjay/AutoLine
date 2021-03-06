# -*- coding: utf-8 -*-

__author__ = "苦叶子"

"""

公众号: 开源优测

Email: lymking@foxmail.com

"""

from flask import Flask
#from flask_bootstrap import Bootstrap
from flask_mail import Mail
#from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_pagedown import PageDown
from config import config

#bootstrap = Bootstrap()
mail = Mail()
#moment = Moment()
db = SQLAlchemy()
#pagedown = PageDown()
trigger = None
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #bootstrap.init_app(app)
    mail.init_app(app)
    #moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #pagedown.init_app(app)

    #app.config["POOL"] = multiprocessing.Pool(processes=app.config['AUTO_PROCESS_COUNT'])

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
