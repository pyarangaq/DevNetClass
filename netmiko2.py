from netmiko import ConnectHandler
from datetime import datetime

cisco1 = {
 "device_type": "cisco_ios",
 "ip": "192.168.153.100",
 "username": "netmiko",
 "password": "netmiko",
 "secret": "netmiko"
}

cisco2 = {
   "device_type": "cisco_ios",
   "ip": "192.168.153.101",
   "username": "netmiko",
   "password": "netmiko",
   "secret": "netmiko"
  }

all_devices = [cisco1, cisco2]

start_time = datetime.now() 
for a_device in all_devices: 
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show ip int brief | ex una")
    print(f"\n\n--------- Device {a_device['device_type']} ---------") 
    print(output)
    print("--------- End ---------")
    end_time = datetime.now()

total_time = end_time - start_time