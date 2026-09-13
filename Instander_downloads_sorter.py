'''
--------------------------
INSTANDER DOWNLOADS SORTER
--------------------------
'''

import os
import shutil


def createFolders(separator='-') -> list:
    folders = []

    for file in os.listdir():
        # Skip directories
        if not os.path.isfile(file):
            continue

        try:
            folder = file.split(separator, 1)[0].strip()

            # Skip invalid/empty folder names
            if not folder:
                print(f"Skipping invalid file: {file}")
                continue

            if not os.path.exists(folder):
                folders.append(folder)

        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue

    folders = list(set(folders))

    # Create folders
    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
        except Exception as e:
            print(f"Could not create folder '{folder}': {e}")

    return folders


def file_sorter(folders: list, files: list) -> None:
    for folder in folders:
        for file in files:

            # Skip directories
            if not os.path.isfile(file):
                continue

            if file.startswith(folder):
                try:
                    destination = os.path.join(folder, file)

                    # Don't move if destination already exists
                    if os.path.exists(destination):
                        print(f"Skipping existing file: {file}")
                        continue

                    shutil.move(file, destination)

                except Exception as e:
                    # Skip files that error out
                    print(f"Skipping '{file}': {e}")
                    continue

        print(f"{folder} completed")


if __name__ == '__main__':
    directory = input("Enter directory path: ").strip()

    try:
        os.chdir(directory)
    except Exception as e:
        print(f"Could not access directory: {e}")
        exit(1)

    original_files = os.listdir()

    sep = input("Enter the separator: ").strip()

    folders = createFolders(sep if sep else '-')

    file_sorter(folders, original_files)

    print("Sorting completed.")
