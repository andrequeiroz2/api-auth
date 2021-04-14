import os
from flask import Flask
from flask_restful import Api
from authenticate.api.oauth.oauth_route import init_oauth_api


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'todo-api/api-auth:1.0'
   
    api = Api(app)  
    init_oauth_api(api)

    return app

