# Import required modules/packages/library
from pprint import pprint

# Open the file and read in the single line of device info
file = open('devices-05.txt', 'r')
file_line = file.readline().strip()

# Display the line I just read
print('Read line: ', file_line)

# Convert to a tuple, using 'split()' to provide a python list
device_info = tuple(file_line.split(','))

# Display a blank line to make easier to read
print('')
# Display a title
print('Input converted to a tuple:')
# Display the dictionary with nice formatting
pprint(device_info)

# Close the file
file.close()
