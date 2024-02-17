"""
-----------------------------
Screenshot & Recording Sorter
-----------------------------
"""
import os


def sortFilesIntoFolders(files) -> None:
    records = []
    screenshots = []
    unknown = []
    # folders = []
    for file in files:
        fileName = file.split('_')
        if not os.path.exists(fileName[0]):
            os.mkdir(fileName[0])

        new_dir = ''
        if fileName[0].lower().startswith('record'):
            records.append(file)
            new_dir = os.path.join(fileName[0], fileName[-1][:10])

        if fileName[0].lower().startswith('screenshot'):
            screenshots.append(file)
            try:
                date_time = fileName[1]
            except IndexError:
                continue
            new_dir = os.path.join(fileName[0], date_time[:10])

        if len(new_dir):
            command = f"move {file} {new_dir}\\"
            print("executing", command)
            if os.path.exists(new_dir):
                os.system(command)
            else:
                os.mkdir(new_dir)
                os.system(command)
                print(f"Moved to {fileName[0]}: {file}")
        else:
            unknown.append(file)
            print(f"Unknown: {file}")
    print(f"Records Found: {len(records)}\nScreenshots Found: {len(screenshots)}\nUnknown Found: {len(unknown)}")


if __name__ == '__main__':
    directory = input("Enter directory path: ")
    # directory = r"D:\phone\Pictures\Screenshots"
    print(f"Changing to Directory: {directory}")
    os.chdir(directory)
    files = os.listdir()
