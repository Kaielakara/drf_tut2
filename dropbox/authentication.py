from rest_framework.authentication import TokenAuthentication as BaseAuthentication

class TokenAutentication(BaseAuthentication):
    keyword = "Bearer"