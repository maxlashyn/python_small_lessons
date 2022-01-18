"""
работа с api
"""

import requests
import json

result = requests.get('https://covid19-eu-data-api-gamma.vercel.app/api/countries?alpha2=de&days=1')
for state in json.loads(result.content):
    for record in state['records']:
        print(f"{record['date']} in {record['nuts_1']} dead {record['deaths']}")