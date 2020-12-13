# White Spaces Remover

import os
import sys

#
# Remove White Spaces
#

def rmWS(command):
	print("Renaming files...")
	filesRenamed = 0
	for fileName in os.listdir():
		# default spaces in the file name is zero and increases afterwards
		spaces = 0
		for alphabet in fileName:
			if alphabet == ' ':
				spaces+=1
		if spaces > 0:
			print(f"Renaming: {fileName}")
			# Replacing white space with underscore
			newFile = fileName.replace(' ','_')
			# Executing command
			os.system(f'{command} \"{fileName}\" \"{newFile}\"')
			print(f"Renamed: {newFile}")
			filesRenamed+=1
		elif spaces == 0:
#			print(f"Skipped: {fileName}")
			continue
	print(f"\n\nSuccessfully Renamed {filesRenamed} of {len(os.listdir())} files, Skipped {len(os.listdir())-filesRenamed} files")

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

osRecog()
