# White Spaces Remover
"""
People Generally create files with white spaces in their names and it creates a hassle if you're in CS department to actually type space
at each file name as it is not supported in most of the platforms.
So I created this script to batch rename my files to reduce the hassle of renaming each file individually and let the program do our job for us.

Instruction:
Copy the program to where ever you want to rename the files on your system and execute the program using python3 and
your files will be renamed to replace the white spaces with underscore
"""
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
                spaces += 1
        if spaces > 0:
            print(f"Renaming: {fileName}")
            # Replacing white space with underscore
            newFile = fileName.replace(' ', '_')
            # Executing command
            os.system(f'{command} \"{fileName}\" \"{newFile}\"')
            print(f"Renamed: {newFile}")
            filesRenamed += 1
        elif spaces == 0:
            # print(f"Skipped: {fileName}")
            continue
    print(
        f"\n\nSuccessfully Renamed {filesRenamed} of {len(os.listdir())} files, Skipped {len(os.listdir()) - filesRenamed} files")


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
