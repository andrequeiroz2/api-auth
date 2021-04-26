import json
import pyrebase
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from requests.models import HTTPError
from .validation import valid_email_passw, valid_body
from firebase_admin._auth_utils import EmailAlreadyExistsError
from config.config import FirebaseConfig


if not firebase_admin._apps:
    cred = credentials.Certificate('fbAdminConfig.json') 
    default_app = firebase_admin.initialize_app(cred)
    pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


def signup_user(body):
    try:
        email = body['email']
        passw = body['passw']
        
        body_num = valid_body(body)
        if body_num > 2:
            example = {"email":"user@user.com", "passw":"123456"}
            body_str = str(body_num)
            inf = "Invadid request: Expected 2 parameters but"+" "+body_str+" "+"were sent"
            resp = {
                "msg": "error",
                "inf": inf,
                "example": example,
                "status": 400
            }
            return resp

        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            example = {"email":"user@user.com", "passw":"123456"}
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "example": example,
                "status": 400
            }
            return resp

        user = auth.create_user(
            email=email,
            password=passw
        )

        resp = {
            "msg": "success",
            "data":[{
                "email":user.email,
                "uid":user.uid,
            }],
            "status":201
        }       
        return resp

    except EmailAlreadyExistsError:
        resp = {
            "msg": "error",
            "inf": "User with the provided email already exists, verify your credentials", 
            "status": 400
        }
        return resp
    
    except Exception as e:
        example = {"email":"user@user.com", "passw":"123456"}
        resp = {
            "msg": "error",
            "inf": "Incorrect request",
            "example": example,
            "status": 400
        }
        return resp


def get_user(body):
    try:
        email = body['email']
        passw = body['passw']

        body_num = valid_body(body)
        if body_num > 2:
            example = {"email":"user@user.com", "passw":"123456"}
            body_str = str(body_num)
            inf = "Invadid request: Expected 2 parameters but"+" "+body_str+" "+"were sent"
            resp = {
                "msg": "error",
                "inf": inf,
                "example": example,
                "status": 400
            }
            return resp


        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            example = {"email":"user@user.com", "passw":"123456"}
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "example": example,
                "status": 400
            }
            return resp
    
        try:
            user = pb.auth().sign_in_with_email_and_password(email, passw)
            resp = {
                "msg": "success",
                "data":[{
                    "email": user['email'],
                    "uid": user['localId'],
                    "token": user['idToken']
                }],
                "status":200
            }       
            return resp
        except HTTPError as e:
            error = json.loads(e.args[1])
            code = error['error']['code']
            inf = error['error']['message']
            resp = {
                "msg": "error",
                "inf": inf,
                "status":code
            }       
            return resp    

    except Exception as e:
        example = {"email":"user@user.com", "passw":"123456"}
        resp = {
            "msg": "error",
            "inf": "Incorrect request",
            "example": example,
            "status": 400
        }
        return resp

   
def delete_user(body):
    try:
        email = body['email']
        passw = body['passw']

        body_num = valid_body(body)
        if body_num > 2:
            example = {"email":"user@user.com", "passw":"123456"}
            body_str = str(body_num)
            inf = "Invadid request: Expected 2 parameters but"+" "+body_str+" "+"were sent"
            resp = {
                "msg": "error",
                "inf": inf,
                "example": example,
                "status": 400
            }
            return resp

        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            example = {"email":"user@user.com", "passw":"123456"}
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "example": example,
                "status": 400
            }
            return resp
        try:
            user = pb.auth().sign_in_with_email_and_password(email, passw)
            uid =  user['localId']
            auth.delete_user(uid)
            resp = {
                "msg": "success",
                "inf": "user deleted",
                "status": 200
            }
            return resp

        except HTTPError as e:
            error = json.loads(e.args[1])
            code = error['error']['code']
            inf = error['error']['message']
            resp = {
                "msg": "error",
                "inf": inf,
                "status":code
            }       
            return resp

    except Exception as e:
        example = {"email":"user@user.com", "passw":"123456"}
        resp = {
            "msg": "error",
            "inf": "Incorrect request",
            "example": example,
            "status": 400
        }
        return resp


def put_user(body):
    try:
        email = body['email']
        passw = body['passw']
        passw_new = body['passw_new']

        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "status": 400
            }
            return resp

        try:
            sign_in = pb.auth().sign_in_with_email_and_password(email, passw)
            auth.update_user(
                email=email,
                uid=sign_in['localId'],
                email_verified=True,
                password= passw_new
            )
    
            resp = {
                "msg": "success",
                "inf": "updated password",
                "status":200
            }       
            return resp

        except HTTPError as e:
            error = json.loads(e.args[1])
            code = error['error']['code']
            inf = error['error']['message']
            resp = {
                "msg": "error",
                "inf": inf,
                "status":code
            }       
            return resp

    except Exception as e:
        example = {"email":"user@user.com", "passw":"123456", "passw_new":"654321"}
        resp = {
            "msg": "error",
            "inf": "Incorrect request",
            "example": example,
            "status": 400
        }
        return resp


def get_token(body):
    try:
        email = body['email']
        passw = body['passw']

        body_num = valid_body(body)
        if body_num > 2:
            example = {"email":"user@user.com", "passw":"123456"}
            body_str = str(body_num)
            inf = "Invadid request: Expected 2 parameters but"+" "+body_str+" "+"were sent"
            resp = {
                "msg": "error",
                "inf": inf,
                "example": example,
                "status": 400
            }
            return resp

        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "status": 400
            }
            return resp

        try:
            user = pb.auth().sign_in_with_email_and_password(email, passw)
            resp = {
                "msg": "success",
                "data":[{
                    "token": user['idToken'],
                    #"registered": user['registered'],
                    "refreshToken": user['refreshToken'],
                    "expiresIn": user['expiresIn']
                }],
                "status":200
            }       
            return resp

        except HTTPError as e:
            error = json.loads(e.args[1])
            code = error['error']['code']
            inf = error['error']['message']
            resp = {
                "msg": "error",
                "inf": inf,
                "status":code
            }       
            return resp    

    except Exception as e:
        example = {"email":"user@user.com", "passw":"123456"}
        resp = {
            "msg": "error",
            "inf": "Incorrect request",
            "example": example,
            "status": 400
        }
        return resp


def login_user(body):
    try:
        email = body['email']
        passw = body['passw']

        body_num = valid_body(body)
        if body_num > 2:
            example = {"email":"user@user.com", "passw":"123456"}
            body_str = str(body_num)
            inf = "Invadid request: Expected 2 parameters but"+" "+body_str+" "+"were sent"
            resp = {
                "msg": "error",
                "inf": inf,
                "example": example,
                "status": 400
            }
            return resp

        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            example = {"email":"user@user.com", "passw":"123456"}
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "example": example,
                "status": 400
            }
            return resp
        try:
            user = pb.auth().sign_in_with_email_and_password(email, passw)
            resp = {
                "msg": "success",
                "data":[{
                    "email": user['email'],
                    "uid": user['localId'],
                    "token": user['idToken']
                }],
                "status":200
            }       
            return resp

        except HTTPError as e:
            error = json.loads(e.args[1])
            code = error['error']['code']
            inf = error['error']['message']
            resp = {
                "msg": "error",
                "inf": inf,
                "status":code
            }       
            return resp

    except Exception as e:
        example = {"email":"user@user.com", "passw":"123456"}
        resp = {
            "msg": "error",
            "inf": "Incorrect request",
            "example": example,
            "status": 400
        }
        return resp
