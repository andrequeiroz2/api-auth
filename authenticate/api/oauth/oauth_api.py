import json
from flask_restful import Resource
from flask import Response, request
from .oauth_controller import signup_user, delete_user, get_user, get_token


#user signup
class OauthSignupApi(Resource):
    def post(self):
        body = request.get_json()
        rs = signup_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])

#user get, delete
class OauthApi(Resource):
    def get(self):
        body = request.get_json()
        rs = get_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])

    def delete(self):
        body = request.get_json()
        rs = delete_user(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])


class OauthTokenApi(Resource):
    def get(self):
        body = request.get_json()
        rs = get_token(body)
        rj = json.dumps(rs)
        return Response(rj, mimetype="application/json", status=rs['status'])


