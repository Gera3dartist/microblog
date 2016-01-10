import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


app = Flask(__name__)
app.config.from_object('config')
app.config['MYSQL_DATABASE_USER'] = 'apps'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dhn3EicNdi'
app.config['MYSQL_DATABASE_DB'] = 'apps'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
db = SQLAlchemy(app)

# configuring loginManager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
# create openid object
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
