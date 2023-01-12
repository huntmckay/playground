import requests
from getpass import getpass

# By using context manager, you can the resources used by
# the session will be released after use

with requests.Session() as session:
    session.auth = ('huntmckay', getpass())

    # Instead of requests.get(), session.get()

    url = 'https://api.github.com'
    response = session.get(f'{url}/user')
    response2 = session.get(f'{url}/user/repos')
    
# You can inspect the response just like before
print(response.headers)
print('This is my first repo!')
print(response2.json()[0]['url'])
# this is breaking with key error, I think its because I have mfa on this account
