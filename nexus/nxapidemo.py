import requests
import json
from pprint import pprint
import re

# login with NX-API CLI
switchuser = 'admin'
switchpassword = 'Admin_1234!'

# define the URL for the NX-API
url = "https://sbx-nxos-mgmt.cisco.com:443/ins"

# define the headers for the HTTP requests
myheaders = {
	"content-type": "application/json",
	"Accept": "application/json"
}

# define the payload for the HTTP POST request
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp nei",
    "output_format": "json"
  }
}

# make the HTTP POST request to the NX-API
response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()

# Login with NX-API REST
auth_url = 'https://sbx-nxos-mgmt.cisco.com:443/api/mo/aaaLogin.json'
auth_body = {
	"aaaUser": {
		"attributes": {
			"name": switchuser,
			"pwd": switchpassword
		}
	}
}

# make the HTTP POST request to the NX-API REST to get the token
auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies={}
cookies['APIC-Cookie'] = token

# set a counter to loop over responses
counter = 0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']

while counter < nei_count:
	hostname = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
	local_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
	remote_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']
	
	body = {
		"l1PhysIf": {
			"attributes": {
				"descr": "Connected to " + hostname + " on " + remote_int
			}
		}
	}

	counter += 1

	if local_int != 'mgmt0':
		int_name = str.lower(str(local_int[:3]))
		int_num = re.search(r'[1-9]/[1-9]*', local_int)
		int_url = 'https://sbx-nxos-mgmt.cisco.com:443/api/mo/sys/intf/phys-['+int_name+str(int_num.group(0))+'].json'
		
		post_response = requests.post(int_url, data=json.dumps(body), headers=myheaders, cookies=cookies, verify=False).json()
		pprint(post_response)