import meraki
import json
from pprint import pprint

token = 'b0dff1a9942701ddfaa17714d0235121e35339b0'
meraki = meraki.DashboardAPI(token)

orgs = meraki.organizations.getOrganizations()

for org in orgs:
	if org['name'] == 'DevNet Sandbox':
		org_id = org['id']

print(f"The Organization ID is: " + org_id)

networks = meraki.organizations.getOrganizationNetworks(org_id)

for network in networks:
	if network['name'] == 'DevNet Sandbox ALWAYS ON':
		network_id = network['id']

print(f"The Network ID is: " + network_id)

vlans_enable = meraki.appliance.updateNetworkApplianceVlansSettings(network_id, vlansEnabled=True)

print(vlans)