#!flask/bin/python
import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_DATABASE_URI

__author__ = 'agerasym'


version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

# path for migration file
migration = SQLALCHEMY_MIGRATE_REPO + \
    ('/versions/{0:03d}_migration.py'.format(version+1))

tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)

# migration script
script = api.make_update_script_for_model(
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
    tmp_module.meta, db.metadata)

# saving migration script
open(str(migration), 'wt').write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('New migration saved as ' + migration)
print('Current database version: ' + str(v))



