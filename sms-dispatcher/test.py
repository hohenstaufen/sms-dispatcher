import requests
import simplejson as json

payload = [
        {
            'number': '+0123456789',
            'text': 'test',
        },
        {
            'number': '+0123456789',
            'text': 'test2',
        },
    ]

headers = {'content-type':'application/json'}

r = requests.post('http://localhost:5000/send', data=json.dumps(payload),
    headers=headers)
