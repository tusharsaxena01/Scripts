# Copy the program to where ever you want the files to be renamed and run the program

import os
import sys

#
# Remove White Spaces
#

def rmWS(command):
	print(f"Renaming files in {os.getcwd()}")
	for fileName in os.listdir():
		print(f"Renaming: {fileName}")
		# Replacing white space with underscore
		newFile = fileName.replace(' ','_')
		# Executing command
		os.system(f'{command} \"{fileName}\" \"{newFile}\"')
		print(f"Renamed: {newFile}")

#
# Linux Operating System
#

def linux():
	print(f"Your Operating System is {sys.platform}")
	command = "mv"
	rmWS(command)
	
#
# Windows Operating System
#

def win():
	print(f'Your Operating System is {sys.platform}')
	command = "ren"
	rmWS(command)
	

# Recognising the operating system

def osRecog():
	if sys.platform.startswith('win32'):
		win()
	elif sys.platform.startswith('linux'):
		linux()

# Executing Program
osRecog()
