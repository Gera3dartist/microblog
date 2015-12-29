from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_object('config')
app.config['MYSQL_DATABASE_USER'] = 'apps'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dhn3EicNdi'
app.config['MYSQL_DATABASE_DB'] = 'apps'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
db = SQLAlchemy(app)

from app import views, models
