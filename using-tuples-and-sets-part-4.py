# Import required modules/packages/library
from pprint import pprint
from collections import namedtuple

# Create named tuple to store information
Dev_info = namedtuple('Dev_info', ['name', 'os', 'ip', 'user',
'password'])

# Create the dictionary
devices = {}

# Open the file and read in the device info
file = open('devices-04.txt', 'r')
for line in file:
    # Add device info into a named tuple
    device_info = Dev_info(*(line.strip().split(',')))

    # Display what we have read and built so far
    print('Device Information: ', device_info)

    # Add the named tuple to a dictionary
    devices[device_info.name] = device_info

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a dictionary of named tuples:')
# Display the tuple with nice formatting
pprint(devices)

#Close the file
file.close()
