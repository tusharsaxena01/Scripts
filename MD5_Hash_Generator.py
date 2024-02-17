import hashlib
#
# pip install pyfiglet
#
import pyfiglet
import os

print(pyfiglet.figlet_format("MD5 Hash Generator"))  # comment if you don't have pyfiglet installed

#
# The Actual program starts from here
#
phrase = input("Enter the Phrase\n> ")
#
# The phrase would be converted to md5 hash and then encoded in utf-8 firmat by default
#
phrase_hash = hashlib.md5(phrase.encode())
print("\nSave to file?(Y/N)\n")
if input("> ") in 'Yy':
    file_n = input("Enter the File Name: ")
    file_name = file_n + ".txt"
    #
    # If the file name does not exist then new file would be created
    #
    ls = os.listdir(os.getcwd())
    if file_name not in ls:
        file = open(file_name, 'a')
        #
        # Converting the md5 hash to a hexadecimal format
        #
        file.write(phrase_hash.hexdigest())
        print("\nHash Saved to %s\\%s" % (os.getcwd(), file_name))
    else:
        print("\nFile Already Exists in %s" % os.getcwd())
#
# the hash would be printed in hexadecimal format
#
print("\nThe Encoded MD5 Hash is: %s\n" % phrase_hash.hexdigest())
