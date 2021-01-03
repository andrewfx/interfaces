import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosxe = driver('10.10.20.175', 'cisco', 'cisco')
iosxe.open()

devices =   ['10.10.20.175',
            '10.10.20.176'
            ]

for device in devices:
    print("Connecting to " + str(device))
    driver = get_network_driver('ios')
    iosxe = driver(device, 'cisco', 'cisco')
    iosxe.open()

    output = iosxe.get_interfaces_ip()
    print (json.dumps(output, indent=4))
    iosxe.close()

    file = open(device, "w")
    file.write(str(output))
    file.close()