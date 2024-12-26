from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint
from router_info import router

# print out which device we are connecting to
print(f"I am connecting to {router["host"]}")

# create a configuration filter
netconf_filter = open("/Users/bumpsinthewire/Documents/Study/DEVASC/devasc/netconf/netconf_filter.xml").read()

# establish a NETCONF connection to the router in a "with" block so that the connection is closed automatically
with manager.connect(
	host=router["host"],
	port=router["port"],
	username=router["username"],
	password=router["password"],
	hostkey_verify=False
) as m:
	# for capability in m.server_capabilities:
	# 	print(capability)
	print("Connected")
	interface_netconf = m.get(netconf_filter)
	print("Getting running config")
	# xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
	# print(xmlDom.toprettyxml(indent="  "))
	# print('*' * 25 + 'Break' + '*' * 50)

	interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
	# pprint(interface_python)
	# name = interface_python["interfaces"]["interface"]["name"]
	# print(name)

	config = interface_python["interfaces"]["interface"]
	op_state = interface_python["interfaces-state"]["interface"]

	print("Reading interface information")
	print(f"Name: {config['name']}")
	print(f"Description: {config['description']}")
	print(f"Packets In: {op_state['statistics']['in-unicast-pkts']}")