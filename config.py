# -*- coding: utf-8 -*-
import os
WTF_CSRF_ENABLED = True
SECRET_KEY = "VERY_SECRET_KEY"

OPENID_PROVIDERS = [
	{"name": "Google", "url": "https://www.google.com/accounts/o8/id"},
	{"name": "Yahoo", "url": "https://me.yahoo.com"},
	{"name": "AOL", "url": "https://openid.aol.com/<username>"},
	{"name": "MyOpenID", "url": "https://www.myopenid.com"},
]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 578
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_USERNAME = str(os.environ.get('MAIL_USERNAME'))+'@gmail.com'
# MAIL_PASSWORD = os.environ.get('MAIL_USERNAME')
MAIL_USERNAME = 'goldbeehoney@gmail.com'
MAIL_PASSWORD = 'goldBeeHoney!'


# administrator list
ADMINS = ['goldbeehoney@gmail.com','gera3dartist@gmail.com','bramwitkowski@yahoo.com']

# pagination
POSTS_PER_PAGE = 3

# site searching

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

################################
##---- languages section -----##
################################

LANGUAGES = {
	'en': "English",
	'uk': "Ukrainian"
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = "microblogaPPl1cat10n"
MS_TRANSLATOR_CLIENT_SECRET = "jtD8ntc9z1L6Fp/o6eMYeeiRjQ2G5vaa1K4mpt59GrI="

###########################
#--- Profiling section ---#
###########################
SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshhold (in seconds)
DATABASE_QUERY_TIMEMOUT = 0.5





