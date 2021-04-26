from flask import Flask
from flask_restful import Api
from authenticate.api.oauth.oauth_route import init_oauth_api
from authenticate.api.oauth.error_405 import errors as error_405
  

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'todo-api/api-auth:1.0'

    api = Api(app, errors=error_405)
    
    init_oauth_api(api)
           
    return app
