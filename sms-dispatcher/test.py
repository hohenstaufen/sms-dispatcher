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

r = requests.post('http://localhost:8000/api/sms/receive', data=json.dumps(payload),
    headers=headers)

i = 0
while i < 30:
	i++
	log = Log()
	log.module = 'test'
	log.type = 'S'
	log.valid = True
	log.inbound = True
	log.sender_name = "prova"
	log.receiver_name = "test"
	log.text = "afdgfdg"
	import datetime
	log.datetime = datetime.datetime.now()
	log.save()
