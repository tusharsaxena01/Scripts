#
#	The Program is only meant for linux users and not windows users
#	Author - github.com/tusharsaxena01
#
try:
	import os
	from termcolor import colored
	s1 = str(f'[{colored("+","green")}]')
	s2 = str(f'[{colored("-","red")}]')
	print(f"{s1} Current Working Directory: {os.getcwd()}")
	choice = input(f"{s1} Want to change it? (Y/N): ")
	if choice in 'yY':
		while True:
			try:
				path = input(f"{s1} Input Full Path: ")
				os.chdir(path)
				break
			except FileNotFoundError:
				print(f"{s2} Invalid Directory")
				continue
	print(f"{s1} Working Directory: {os.getcwd()}")
	while True:
		try:
			downloaded = list()
			package = input(f"{s1} Press (Ctrl + C) to Exit. Input the package name: ")
			status = os.system(f'apt download {package}')
			if status == 0:
				downloaded.append(package)
			else:
				print(f"{s2} Error Occured!")
				print(f"{s2} Invalid Package! \'{package}\'")
		except KeyboardInterrupt:
			if len(downloaded) != 0:
				print(f"\n{s1} Displaying all Downloaded Packages: ")
				for download in downloaded:
					print(f"{s1} {download}")
				print(f"{s1} Exiting...")
			break
except ModuleNotFoundError:
	import os
	import sys
	import socket as s
	print("Neccessary Modules Not Found! Downloading...")
	ip_address = s.gethostbyname(s.gethostname())
	if ip_address == "127.0.0.1":
		print("No Internet Connectivity!")
	else:
		if sys.platform.startswith('win32'):
			print("This Program is Only for Linux Users!")
			sys.exit(0)
		else:
			if sys.version.startswith('3'):
				os.system('pip3 install termcolor')
			else:
				os.system('pip install termcolor')
