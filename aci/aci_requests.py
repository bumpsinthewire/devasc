import requests
import json


# login to APIC and get token
url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

payload = {
	  "aaaUser": {
		  "attributes": {
			  "name": "admin",
			  "pwd": "!v3G@!4@Y"
		  }
    }
}

headers = {
	'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token


# Get application profile
url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Power_up.json"

get_response = requests.get(url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))


# Change description of application profile
post_payload = {
	"fvAp": {
		"attributes": {
			"descr": "",
			"dn": "uni/tn-Heroes/ap-Power_up"
		}
	}
}

post_response = requests.post(url, headers=headers, cookies=cookie, data=json.dumps(post_payload), verify=False).json()

get_response = requests.get(url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))