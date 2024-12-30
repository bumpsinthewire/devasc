import requests
import json
from pprint import pprint

url = "https://api.meraki.com/api/v1/organizations"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': 'b0dff1a9942701ddfaa17714d0235121e35339b0'
}

response = requests.get(url, headers=headers, data=payload).json()

pprint(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
	if response_org['name'] == 'DevNet Sandbox':
		org_id = response_org['id']

print(f"The Organization ID is: " + org_id)