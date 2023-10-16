# Import required modules/packages/library
from pprint import pprint

# Create the device_info list
device_info = {}

# Open the file and read the single line of device info
file = open('devices-03.txt', 'r')
file_line = file.readline().strip()

# Display the line from the file
print('Read line: ', file_line)

# Use the string 'split' function to convert
# the comma-separated string into a list of items
device_info_list = file_line.split(',')

# Now put those items from the list into our dictionary
device_info['name'] = device_info_list[0]
device_info['os-type'] = device_info_list[1]
device_info['ip'] = device_info_list[2]
device_info['username'] = device_info_list[3]
device_info['password'] = device_info_list[4]

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a dictionary:')
# Display the dictionary with nice formatting
pprint(device_info)

# Close the file
file.close()
