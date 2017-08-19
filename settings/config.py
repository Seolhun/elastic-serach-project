# File Path Config
BASE_NAME="/Users/HunSeol/Desktop/"

# Flask Settings
FLASK_SERVER_NAME = 'localhost:5000'
FLASK_DEBUG = True  # Do not use debug mode in production

# SQLAlchemy Settings
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hooney:blue1220@@127.0.0.1/buzzni'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:blue1220@@127.0.0.1/buzzni'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# MongoDB Settings
MONGO_USERNAME = 'shooney'
MONGO_PASSWORD = 'blue1220@'
# MONGO_HOST = '192.168.0.2'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DBNAME = 'buzzni'

# MongoDB Settings
ELASTIC_SEARCH_HOST = '127.0.0.1:9200'

# Page Config
MAX_PER_PAGE = 5

# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }