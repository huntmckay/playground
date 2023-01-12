import requests
from requests.exceptions import Timeout

url = 'https://api.github.com'

try:
    resp = requests.get(url, timeout=(1))
except Timeout:
    print('The Request timed out')
else:
    print('The Request did not time out')
