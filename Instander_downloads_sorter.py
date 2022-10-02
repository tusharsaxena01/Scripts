'''
--------------------------
INSTANDER DOWNLOADS SORTER
--------------------------
'''
def createFolders(sep = '-'):
    name = ""
    folders = []
    # finding folder names
    for file in os.listdir():
        file = file.split(sep)
        if not os.path.exists(file[0]):
            folders.append(file[0])
    folders = list(set(folders))
    # creating folders
    for folder in folders:
        os.mkdir(folder)
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
    folders = createFolders(sep = input("Enter the sepearator: "))
    file_sorter(folders, original_files)
