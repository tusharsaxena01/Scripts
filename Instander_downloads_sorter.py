'''
--------------------------
INSTANDER DOWNLOADS SORTER
--------------------------
'''
import os


def createFolders(seperator='-') -> list:
    folders = []
    # finding folder names
    for file in os.listdir():
        file = file.split(seperator)
        if not os.path.exists(file[0]):
            folders.append(file[0])
    folders = list(set(folders))
    # creating folders
    for folder in folders:
        os.mkdir(folder)
    return folders


def file_sorter(folders: list, files: list) -> None:
    for folder in folders:
        for file in files:
            if file.startswith(folder):
                os.system(f"move {file} {folder}/{file}")
        print(f"{folder} completed")


if __name__ == '__main__':
    directory = input("Enter directory path: ")
    os.chdir(directory)
    original_files = os.listdir()
    sep = input("Enter the separator: ")
    folders = createFolders(sep if sep else '-')
    file_sorter(folders, original_files)
