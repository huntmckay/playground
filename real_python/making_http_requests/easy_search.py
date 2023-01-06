import requests

resp = requests.get(

    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},

)

json_resp = resp.json()
repository = json_resp['items'][0]
print(f'Text matches: {repository["text_matches"][0]}')
# print(f'Repository name: {repository["name"]}')
# print(f'Repository description: {repository["description"]}')
