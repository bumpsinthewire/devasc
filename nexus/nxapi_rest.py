import requests
import json
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
})

headers = {
  'Content-Type': 'application/json',
  'Cookie': 'APIC-cookie=D/j2nAW0OrnYjcYc97t6K+i9UFUDGaZnNppzGEuqqic5SXsMBymec1F+zLCFdKdBNlcgnViQjl/fYWHlaVy2e0XV194v4Wh9PMll/OuNhxyIT8WfM1d2N7HDnrzCRv/yVAxdoDyCxFCli7KjdWg6NjZlpu2qWlWBqoDJ4sFco/U=; nxapi_auth=dzqnf:J4LlWuV3mL/1EkGMkIYEzvgx+RM='
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()

pprint(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token


# now doing a PUT request to change the description of the interface
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/33].json"

payload = json.dumps({
  "l1PhysIf": {
    "attributes": {
      "descr": "this was done with python"
    }
  }
})

headers = {
  'Content-Type': 'application/json',
}

put_response = requests.put(url, headers=headers, data=payload, cookies=cookies, verify=False).json()

pprint(put_response)