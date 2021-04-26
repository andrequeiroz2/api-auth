from typing import Dict
from email_validator import validate_email, EmailNotValidError


def valid_email_passw(email, passw):
    
    if not email and not passw:
        inf={"error":"Enter a valid email address and password"}
        return inf
    if not email:
        inf={"error":"Enter a valid email address"}
        return inf
    if not passw:
        inf={"error":"Enter a password"}
        return inf
    if len(passw) < 6:
        inf={"error":"Enter a minimal 6 digts for password"}
        return inf
    try:
        validate_email(email)
        inf = {"success":"success"}
        return inf
    except EmailNotValidError as e:
        inf = {"error": "Email invalid"}
        return inf 
    

def valid_body(body):
    count = 0
    for i in enumerate(body):
        count += 1
    return count