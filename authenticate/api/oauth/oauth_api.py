import json
from flask_restful import Resource
from flask import Response, request
from .oauth_controller import (
    signup_user, 
    delete_user, 
    get_user, 
    get_token, 
    put_user, 
    login_user
)


#user signup
class OauthSignupApi(Resource):
    def post(self):
        body = request.get_json()
        rs = signup_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])

#user login
class OauthLoginApi(Resource):
    def post(self):
        body = request.get_json()
        rs = login_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])
    

class OauthApi(Resource):
    #user get
    def post(self):
        body = request.get_json()
        rs = get_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])

    #user delete
    def delete(self):
        body = request.get_json()
        rs = delete_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])

    #user put
    def put(self):
        body = request.get_json()
        rs = put_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])


#user get token
class OauthTokenApi(Resource):
    def post(self):
        body = request.get_json()
        rs = get_token(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])


