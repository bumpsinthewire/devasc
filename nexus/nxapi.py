import requests
import json

target = "http://sbx-nxos-mgmt.cisco.com:80/ins"
username = "admin"
password = "Admin_1234!"

request_headers = {"content-type": "application/json"}
showcmd = {
	"ins_api": {
		"version": "1.0",
		"type": "cli_show",
		"chunk": "0",
		"sid": "1",
		"input": "show version",
		"output_format": "json"
	}
}

response = requests.post(
	target,
	data=json.dumps(showcmd),
	headers=request_headers,
	auth=(username, password),
	verify=False
).json()

print(json.dumps(response, indent=2, sort_keys=True))