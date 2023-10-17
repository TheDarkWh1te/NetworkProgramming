# Import required modules/packages/library
from pprint import pprint
from collections import namedtuple

# Create named tuple to store information
Dev_info = namedtuple('Dev_info', ['name', 'os_type', 'ip', 'user','password'])

# Create a set for holding OS types
os_types = set()

# Open the file and read in the device info
file = open('devices-04.txt', 'r')
for line in file:
    # Add device info into a named tuple
    device_info = Dev_info(*(line.strip().split(',')))

    # Display what we have read and built so far
    print('Device Information: ', device_info)

    # Add the OS type to the set holding all OS types
    if device_info.os_type not in os_types:
        os_types.add(device_info.os_type)

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a set of OS types present:')
# Display the tuple with nice formatting
pprint(os_types)

# Close the file
file.close()
