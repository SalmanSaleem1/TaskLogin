from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from face.configs import BaseConfig
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = True


app = Flask(__name__, template_folder='template')
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)

mail = Mail(app)


from face.user.Routes import users
from face.post.Routes import posts
from face.main.Rout import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)



# def create_app(config_class=configs):
    # app = Flask(__name__, template_folder='template')
    # app.config.from_object(BaseConfig)
    #
    # db.init_app(app)
    # bcrypt.init_app(app)
    # mail.init_app(app)
    # login_manager.init_app(app)
    # login_manager.init_app(app)
    # login_manager.init_app(app)

    # from face.user.Routes import users
    # from face.post.Routes import posts
    # from face.main.Rout import main
    #
    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    # app.register_blueprint(main)

    # return app