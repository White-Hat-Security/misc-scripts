from netmiko import ConnectHandler

 
#First create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': '',
    'username': '',
    'password': '',
    'secret':''
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
 
#Discover the hostname from the prompt 
net_connect.enable()
 
hostname = net_connect.send_command('show run | i hostname')
hostname.split("  ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)
 
filename = '/home/router-' + device
# to save backup to same folder as script use below line and comment out above line 
 
showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")   # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
 
# Finally close the connection
net_connect.disconnect()


