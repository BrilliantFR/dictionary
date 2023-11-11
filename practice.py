import requests

api_key = 'ab0f6e94-a668-4218-8e35-5fe4985278dc'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definitions)