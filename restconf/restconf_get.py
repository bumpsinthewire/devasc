import requests
import json
from pprint import pprint

# set up connection parameters in a dictionary
router = {
	"ip": "devnetsandboxiosxe.cisco.com",
	"port": "443",
	"username": "admin",
	"password": "C1sco12345"
}

# set REST API headers
headers = {
	"Accept": "application/yang-data+json",
	"Content-Type": "application/yang-data+json"
}

# set REST API URL path
url = f"https://{router['ip']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, auth=(router['username'], router['password']), verify=False)

api_response = response.json()
print("/" * 50)
pprint(api_response["ietf-interfaces:interface"][0]["description"])
print("/" * 50)
if api_response["ietf-interfaces:interface"][0]["enabled"]:
	print("Interface is enabled.")