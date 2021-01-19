#	Check if the device is connected to the internet

'''	This is the shortest and easiest method I could find	'''

import socket

# getting IP address and comparing it into the localhost IP address
# ip = socket.gethostbyname(socket.gethostname())

if (socket.gethostbyname(socket.gethostname()) == '127.0.0.1'):
	print("Not Connected to the internet")
else:
	print("Connected to the internet")
