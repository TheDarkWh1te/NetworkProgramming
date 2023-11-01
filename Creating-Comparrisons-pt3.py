#Import required modules/packages/library
import re

# Display heading
print('')
print('Devices and their Management IP addresses')
print('-----------------------------------------')

# Create regular expression to find the Mgmt IP address
ip_addr_pattern = re.compile(r'Mgmt:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# Read all lines of device information from file
file = open('devices-06.txt', 'r')
for line in file:
    # Put device info into list
    device_info_list = line.strip().split(',')

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]

    # Find the Mgmt IP address from the line in the file,
    # and put it into device_info
    mgmt_addr = ip_addr_pattern.search(line)
    device_info['ip'] = mgmt_addr.group(1)

    # Display device and management IP address
    print(' Device:', device_info['name'],' Mgmt IP:', device_info['ip'])

# Display a blank line to make easier to read
print('')

#close file
file.close()
