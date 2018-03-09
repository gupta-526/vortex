from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from config import SQLALCHEMY_DATABASE_URI
from flask import Flask
from run import flask_app as app
from app.models import db

# db_username = 'purnimakumar'
# db_password = ''
# db_name = 'cvizdb'
# db_hostname = 'localhost'
# SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=db_username,
# 																						DB_PASS=db_password,
# 																						DB_ADDR=db_hostname,
# 																						DB_NAME=db_name)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()