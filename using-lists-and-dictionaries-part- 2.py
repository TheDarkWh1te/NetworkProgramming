# Import required modules/packages/library
from pprint import pprint

# Create the device_info list
device_info = []

# Open the file and read the single line of device info
file = open('devices-03.txt', 'r')
file_line = file.readline().strip()

# Display the line from the file
print('Read line: ', file_line)

# Use the string 'split' function to convert
# the comma-separated string into a list of items
device_info = file_line.split(',')

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a list:')
# Display the list with nice formatting
pprint(device_info)

# Close the file
file.close()
