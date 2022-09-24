'''
--------------------------
INSTANDER DOWNLOADS SORTER
--------------------------
'''
def createFolders(sep = '-'):
    name = ""
    folders = []
    # finding folder names
    for dir in os.listdir():
        for d in dir:
            if d == sep:
                folders.append(name)
                name = ""
                break
            else:
                name+=d
    folders = set(folders)
    # creating folders
    for f in folders:
        os.system(f"mkdir {f}")
    return folders

def file_sorter(folders, files):
    for folder in folders:
        for file in files:
            if file.startswith(folder):
                os.system(f"move {file} {folder}/{file}")
        print(folder)
        
        
if __name__ == '__main__':
    import os
    directory = input("Enter directory path: ")
    os.chdir(directory)
    original_files = os.listdir()
    folders = createFolders(seperator = input("Enter the sepearator: "))
    file_sorter(folders, original_files)
    
