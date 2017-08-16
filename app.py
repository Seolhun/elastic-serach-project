# Buzzni setting information
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from api import LOGO
from api.goods.views import Goods, GoodsList
from settings import base_config as conf, import_data
# Buzzni Database Config
from settings.database import db, mongo
from settings.logging import logger

app = Flask(__name__)
cors = CORS(resources={r"/api/*": {"origins": "*"}})
# Add Resources Part
api = Api(app, prefix="/api/v1")

# Stack Part
api.add_resource(Goods, '/goods/<int:pid>')
api.add_resource(GoodsList, '/goods')


def configure_app(flask_app):
    flask_app.config['FLASK_SERVER_NAME'] = conf.FLASK_SERVER_NAME
    flask_app.config['FLASK_DEBUG'] = conf.FLASK_DEBUG

    # MariaDB SQLAlchemy Configuration
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = conf.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = conf.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SQLALCHEMY_ECHO'] = conf.SQLALCHEMY_ECHO

    # MongoDB PyMongo Configuration
    # flask_app.config['MONGO_USERNAME'] = conf.MONGO_USERNAME
    # flask_app.config['MONGO_PASSWORD'] = conf.MONGO_PASSWORD
    flask_app.config['MONGO_HOST'] = conf.MONGO_HOST
    flask_app.config['MONGO_PORT'] = conf.MONGO_PORT
    flask_app.config['MONGO_DBNAME'] = conf.MONGO_DBNAME


def initialize_app(flask_app):
    # Init MariaDB
    db.init_app(flask_app)

    # Create Database When generated First Request
    @app.before_first_request
    def create_tables():
        db.create_all()
        import_data.generate_data()

    # Init MongoDB
    mongo.init_app(flask_app, config_prefix='MONGO')

    # Init RESTful API
    api.init_app(flask_app)
    cors.init_app(flask_app)

if __name__ == '__main__':
    configure_app(app)
    initialize_app(app)
    print(LOGO)

    logger.info('Starting development server at http://{}/api/ <<<<<'.format(app.config['FLASK_SERVER_NAME']))
    app.run(port=5000, debug=True)
