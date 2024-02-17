#
#	Rot-13 Algorithm Encryptor and Decryptor
#
#   -----------------------------------------------------
#
#       External Module so creating an exception block for it
#
try:
    import pyfiglet

    module = 1
except ModuleNotFoundError:
    print("pyfiglet not installed\n Install using \npip install pyfiglet")
    module = 0
import os

if not module == 0:
    print(pyfiglet.figlet_format("ROT-13"))
s = str("[+]")  # for information
s1 = str("[-]")  # for warning
#	all the valid alphabets
alphabets = "abcdefghijklmnopqrstuvwxyz"
#	all substitute for alphabet in rot 13 algorithm
rot = "nopqrstuvwxyzabcdefghijklm"
author = "Tushar Saxena"


#
#	Encryptor
#
def encrypt():
    n_text = str(input("%s Enter Text: " % s))
    e_text = ""
    for n in range(0, len(n_text)):
        m = 0
        while m in range(0, len(alphabets)):
            if n_text[n] == alphabets[m].upper():
                e_text = e_text + rot[m].upper()
            elif n_text[n] == alphabets[m]:
                e_text = e_text + rot[m]
            m += 1
    save = input("%s Save To a file? (Y/N): " % s)
    if save in 'Yy':
        f_n = input("%s Enter the file name: " % s)
        f_name = f_n + '.txt'
        ldir = os.listdir()
        if f_name in ldir:
            print("%s File Already Exists!" % s1)
            overwrite = input("%s Overwrite? (Y/N): " % s)
            if overwrite in 'Yy':
                file_name = open(f_name, 'w')
                file_name.write(e_text)
                file_name.close()
            elif overwrite in 'Nn':
                n = 1
                file_letter = f_n
                while f_name in ldir:
                    m = str(n)
                    f_name = f"{file_letter}({m}).txt"
                    n += 1
                    print(f_name)
                file_name = open(f_name, 'a')
                file_name.write(e_text)
                file_name.close()
            else:
                print("%s Invalid Input!" % s1)
                print("%s File would not be saved!" % s1)
        else:
            file_name = open(f_name, 'a')
            file_name.write(e_text)
            file_name.close()
            print("%s Your file is saved to %s\\%s" % (s, os.getcwd(), f_name))
    print("%s Your Encrypted Text: %s" % (s, e_text))


author = "Tushar Saxena"


#
#	Decryptor
#
def decrypt():
    sel = input("%s Read from file? (Y/N): " % s)
    n_text = ""
    if sel in 'Yy':
        ch = input("%s Is Your file in %s? (Y/N): " % (s, os.getcwd()))
        if ch in 'yY':
            print("%s Directory Choosen: %s" % (s, os.getcwd()))
        elif ch in 'Nn':
            directory = input("%s Enter the Full Directory: ")
            os.chdir(directory)
        f_n = input("%s Enter File Name (Extension is always taken .txt): " % s)
        f_name = f"{f_n}.txt"
        ldir = os.listdir()
        if f_name in ldir:
            file_name = open(f_name, 'r')
            e_text = file_name.read()
        else:
            print("%s %s does not exist!" % (s1, f_name))
            e_text = input("%s Enter the Encrypted Text: " % s)
    else:
        ch = 'n'
        e_text = input("%s Enter the Encrypted Text: " % s)
    for n in range(0, len(e_text)):
        m = 0
        while m in range(0, len(rot)):
            if e_text[n].isupper() and e_text[n] == rot[m].upper():
                n_text = n_text + alphabets[m].upper()
            elif e_text[n] == rot[m]:
                n_text = n_text + alphabets[m]
            m += 1
    if ch in 'Yy':
        file_name.close()
    print("%s Your Text is: %s" % (s, n_text))


author = "Tushar Saxena"


#
#	Choice Selection
#
def choice():
    print("%s Choose:\n%s\t1. Encryptor\n%s\t2. Decryptor\n%s\t3. Exit" % (s, s, s, s))
    ch = int(input("%s : " % s))
    if ch == 1:
        encrypt()
    elif ch == 2:
        decrypt()
    else:
        quit()


#
#	Calling the Primary Function
#
choice()
print("\t-Program Created By %s" % author)
quit()
