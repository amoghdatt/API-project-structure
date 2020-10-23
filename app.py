from flask import Flask
from flask_restful import Api
from cfs.resources import CFS
from cfs.config import DevelopmentConfig, TestingConfig

def create_app(config:str='development') -> Flask:

    app = Flask(__name__, instance_relative_config=True)
    if(config == 'development'):
        app.config.from_object(DevelopmentConfig)
    elif(config == 'testing'):
        app.config.from_object(TestingConfig)
    else:
        app.config.from_pyfile('config.py', silent=True)
    api = Api(app)
    api.add_resource(CFS,'/cfs',endpoint="cfs")
    return app