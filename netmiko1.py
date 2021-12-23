#import modules
from netmiko import ConnectHandler
# device info in dictionary format.
device_config = {
 "device_type": "cisco_ios",
 "ip": "192.168.153.101",
 "username": "netmiko",
 "password": "netmiko",
 "secret": "netmiko"
}

net_connect = ConnectHandler(**device_config) 

config_commands = ["int e0/1",
                   "ip addr 100.100.100.2 255.255.255.0",
                   "no shut",
                   "exit"
                   ]
output = net_connect.send_config_set(config_commands)
output = net_connect.save_config(cmd="wr mem")
output = net_connect.send_command("sh ip int brief | ex una")
print(output)