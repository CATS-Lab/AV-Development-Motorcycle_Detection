# import argparse
import os
import sys
from pathlib import Path

import cv2

import time


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # VMT project root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


def list_directory(root, subdirs=[]):
    # Get subdirectories
    for path in Path(root).iterdir():
        if path.is_dir():
            subdirs.append(f'{path}')
            list_directory(path, subdirs)
    return subdirs[1:]
 
def list_file(root):
    # Subdirectories
    dir_list = list_directory(root)

    # Get all file's addresses
    files = []
    for dir in dir_list:
        file_path = os.listdir(dir)

        # Remove ./data/raw from the addresses
        dir = os.path.relpath(dir, root)

        for file in file_path:
            files.append(f'{dir}/{file}')
            
    return files


def extract_frame(video_path):
    video = cv2.VideoCapture(f'{ROOT}/data/raw/{video_path}')

    # Used as counter variable
    count = 0
    # checks whether frames were extracted
    success = 1

    # Created directory if it does not exist
    path = os.path.join(f'{ROOT}/data/frames/{video_path}')
    if not os.path.exists(path):
        os.makedirs(path)  

    while success:
  
        # video object calls read
        # function extract frames
        success, image = video.read()
  
        # Saves the frames with frame-count
        # print(f'{path}/{count}.jpg')
        cv2.imwrite(f'{path}/{count}.jpg', image)
        print(f'{video_path}: Extract frame {count}.')
  
        count += 1
        time.sleep(1)



def main():
    # path = f'157820 - Leesburg PTMS & TTMS/CR 44 (117024)/15782017.mp4'
    # extract_frame(path)
    list = list_file(f'{ROOT}/data/raw/')
    for x in list:
        # print("x::::::::::::", x)
        extract_frame(x)
        

if __name__ == "__main__":
    main()