import os


class FirebaseConfig():
    apiKey=os.environ.get("apiKey")
    authDomain=os.environ.get("authDomain")
    databaseURL=os.environ.get("databaseURL")
    projectId=os.environ.get("projectId")
    storageBucket=os.environ.get("storageBucket")
    messagingSenderId=os.environ.get("messagingSenderId")
    appId=os.environ.get("appId")
