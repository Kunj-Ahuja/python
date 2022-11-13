import requests
response = requests.get('https://v2.jokeapi.dev/joke/Dark').json()
if response['type'] == 'single':
    print(response['joke'])
else:
     print(response['setup'])
     print('>> ' + response['delivery'])