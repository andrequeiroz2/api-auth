from flask_restful import Api
from authenticate.api.oauth.error_405 import errors as error_405


api = Api()


def init_api(app):
    
    from authenticate.api.oauth.oauth_route import init_oauth_api
    api = Api(app, errors= error_405,)

    init_oauth_api(api)

  



  