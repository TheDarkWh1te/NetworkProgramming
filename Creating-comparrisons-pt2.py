# Display heading
print('')
print('Devices with bad software versions')
print('----------------------------------')

# Set Variable for current version comparison used in Step 4
current_version = 'Version 5.3.1'

# Read all lines of device information from file
file = open('devices-06.txt', 'r')
for line in file:
    # Put device info into list
    device_info_list = line.strip().split(',')

# Put device information into dictionary for this one device
device_info = {} # Create the inner dictionary of device info
device_info['name'] = device_info_list[0]
device_info['ip'] = device_info_list[2]
device_info['version'] = device_info_list[3]

    #If the version doesn't match our 'current version',
    # display a warning
    if device_info['version'] != current_version:
        print(' Device:', device_info['name'],' Version:', device_info['version'])
        
# Display a blank line to make easier to read
print('')
# Close the file
file.close()
