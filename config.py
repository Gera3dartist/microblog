import os

__author__ = 'agerasym'


WTF_CSRF_ENABLED = True
SECRET_KEY = 'some+V3RYSeCR3TKey'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://apps:Dhn3EicNdi@localhost/apps'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'https://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'https://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
]

# database config
# MYSQL_DATABASE_USER = 'apps'
# MYSQL_DATABASE_PASSWORD = 'Dhn3EicNdi'
# MYSQL_DATABASE_DB = 'apps'
# MYSQL_DATABASE_HOST = 'localhost'

# SQL_ALCHEMY_DATABASE_URI =


