from .oauth_api import (
    OauthApi,
    OauthSignupApi,
    OauthTokenApi
)

def init_oauth_api(api):
    api.add_resource(OauthSignupApi, "/api/users/auth/signup")
    api.add_resource(OauthTokenApi, "/api/users/auth/token")
    api.add_resource(OauthApi, "/api/users/auth")
