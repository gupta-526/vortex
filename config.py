import os

basedir = os.path.join(os.path.dirname(__file__))
db_username = 'purnimakumar'
db_password = ''
db_name = 'vortex'
db_hostname = 'localhost'

DEBUG=True
PROPAGATE_EXCEPTIONS=True
TRAP_BAD_REQUEST_ERRORS = True
SECRET_KEY='harryPotterAndTheGobletOfFire'
UPLOAD_FOLDER = os.path.join(basedir,'uploads')
ALLOWED_EXTENSIONS = set(['txt'])
# PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
HOST_NAME="127.0.0.1"
PORT=5000
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "migrations")
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=db_username,
																						DB_PASS=db_password,
																						DB_ADDR=db_hostname,
																						DB_NAME=db_name)



