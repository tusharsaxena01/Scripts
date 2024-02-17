#       importing necessary modules
import os
import sys

#       checking the operating system for compatibility
if not sys.platform.startswith('win32'):
    print("The Program is only Meant for Windows Operating System")
else:
    print("Shutdown Your Computer on your desired time!")
    choice = int(input("1. Seconds\n2. Minutes\n3. Hours\n> "))
    time = int(input("Enter the Amount of Time to shutdown Your PC: "))
    #	Converting the time amount in seconds
    if choice == 3:
        timeSeconds = time * 60 * 60
    elif choice == 2:
        timeSeconds = time * 60
    elif choice == 1:
        timeSeconds = time
    else:
        print("Invalid Input! Default Time = 1 Second")
        timeSeconds = 1
    #	Creating the command
    command = f'shutdown.exe /s /t {timeSeconds}'
    os.system(f'cmd /c "{command}"')
    #       Abort the shutdown using "shutdown -a"
    print("To abort the Shutdown Use \"shutdown -a\"")
    quit()
