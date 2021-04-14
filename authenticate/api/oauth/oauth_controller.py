import json
import pyrebase
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from .validation import valid_email_passw
from firebase_admin._auth_utils import EmailAlreadyExistsError, UserNotFoundError


if not firebase_admin._apps:
    cred = credentials.Certificate('fbAdminConfig.json') 
    default_app = firebase_admin.initialize_app(cred)

    pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


def signup_user(body):
    try:
        email = body['email']
        passw = body['passw']

        valid = valid_email_passw(email, passw)
        if "error" in valid.keys():
            resp = {
                "msg": "error",
                "inf": valid['error'],
                "status": 400
            }
            return resp

        user = auth.create_user(
            email=email,
            password=passw
        )

        data = {
            "email": email,
            "uid": user.uid,
            
        }
        resp = {
            "msg": "success",
            "data":[{
                "email":user.email,
                "uid":user.uid,
            }],
            "status":200
        }       
        return resp

    except EmailAlreadyExistsError:
        resp = {
            "msg": "error",
            "inf": "User with the provided email already exists",
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
        except Exception as e:
            resp = {
                "msg": "error",
                "inf": "User not found",
                "data":[{
                }],
                "status":400
            }       
            return resp

        resp = {
            "msg": "success",
            "data":[{
                "email": user['email'],
                "uid": user['localId'],
            }],
            "status":200
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
        except Exception as e:
            resp = {
            "msg": "error",
            "inf": "User not found",
            "data":[{
            }],
            "status":400
            }       
            return resp
        
        uid =  user['localId']
        auth.delete_user(uid)
        
        resp = {
            "msg": "success",
            "inf": "user deleted",
            "status": 200
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


def get_token(body):
    try:
        email = body['email']
        passw = body['passw']

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
        except Exception as e:
            resp = {
                "msg": "error",
                "inf": "User not found",
                "data":[{
                }],
                "status":400
            }       
            return resp

        resp = {
            "msg": "success",
            "data":[{
                "token": user['idToken'],
                "registered":user['registered'],
                "refreshToken":user['refreshToken'],
                "expiresIn":user['expiresIn']
            }],
            "status":200
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

   