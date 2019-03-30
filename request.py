import requests
import json

# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

apiKey = 'cd74d568016ce9a5060f8d05719375e7'

url = 'http://api.reimaginebanking.com/atms?key=cd74d568016ce9a5060f8d05719375e7'
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,
}
# Create a Savings Account
response = requests.post(url)

if response.status_code == 201:
	print('account created')


print(response)