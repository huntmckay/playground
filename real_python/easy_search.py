import requests

resp = requests.get(

    'https://api.github.com/search/repositories',
    params={'q': 'schedule+language:python'}

)

json_resp = resp.json()

repository = json_resp['items'][0]
print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')
