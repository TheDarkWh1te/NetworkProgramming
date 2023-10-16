# Import required modules/packages/library
from pprint import pprint

# For simplicity we will create our outer dictionary and lists
devices = {} # Create the outer dictionary for all OS-types
devices['ios'] = [] # Create initial empty list of devices
devices['nx-os'] = [] # Create initial empty list of devices
devices['ios-xr'] = [] # Create initial empty list of devices

# Open the file and read the list of device info
file = open('devices-04.txt', 'r')
for line in file:
    # Get device info into list
    device_info_list = line.strip().split(',')

    # Put device information into dictionary for this one device
    device_info = {} # Create the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]

    # Display what we have read and built so far
    print('Read device information: ', device_info)

    # Now place our device and its info onto the correct list of devices,
    # in our main OS-type dictionary, based on the device's OS-type.
    devices[device_info['os-type']].append(device_info)

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a dictionary with OS sorting:')
# Display the dictionary with nice formatting
pprint(devices)

# Close the file
file.close()
