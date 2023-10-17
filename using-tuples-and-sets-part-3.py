# Import required modules/packages/library
from pprint import pprint

# Create the outer list for all devices
devices = []

# Open the file and read in the device info
file = open('devices-04.txt', 'r')
for line in file:

    # Add device info into tuple
    device_info = tuple(line.strip().split(','))

    # Display what we have read and built so far
    print('Read line: ', device_info)

    # Append our device and its info onto our 'devices' list
    devices.append(device_info)

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a list tuples:')
# Display the tuple with nice formatting
pprint(devices)

# Close the file
file.close()
