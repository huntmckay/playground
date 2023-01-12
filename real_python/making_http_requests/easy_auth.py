import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__ (self, r):
        """Attach an API to custom auth header."""

        r.headers['X-TokenAuth'] = f'{self.token}'   #python 3.6+
        return r

resp = requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde' ))
print(resp)
