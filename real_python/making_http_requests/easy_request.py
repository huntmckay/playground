import requests
from requests.exceptions import HTTPError


for url in ['https://api.github.com/','https://api.github.com/invalid']:
    try:

        resp = requests.get(url)
        
        # if the response was successful, no exception will raise
        resp.raise_for_status()
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')
    else:
        print(f'request to "{url}" Successful')
