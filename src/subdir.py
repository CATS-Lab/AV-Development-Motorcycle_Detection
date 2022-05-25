import os
from pathlib import Path
 
def list_directory(root, subdirs=[]):
    # Get subdirectories
    for path in Path(root).iterdir():
        # print("1", path)
        # path = os.path.relpath(path, root)
        # print("2", path)
        if path.is_dir():
            subdirs.append(f'{path}')
            list_directory(path, subdirs)
    return subdirs[1:]
 


def list_file(root):
    # Subdirectories
    dir_list = list_directory(root)

    # Get all file's addresses
    file_list = []
    for dir in dir_list:
        file_path = os.listdir(dir)

        # Remove ./data/raw from the addresses
        dir = os.path.relpath(dir, root)

        for file in file_path:
            file_list.append(f'{dir}/{file}')
            
    return file_list


rootdir = './data/raw'
file_list = list_file(rootdir)

for x in file_list:
    print(x)
    