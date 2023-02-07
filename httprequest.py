from helper import validate
import requests
from pprint import pprint


while True:
    word = input('Write a word: ')
    if not word:
        break
    if validate(word):
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    else:
        continue
    response = requests.get(url)
    if response.status_code == 200:
        words = response.json()
    for definition in words:
        print(definition['phonetics'][1]['audio'])
    #import json -> json.dumps(words)