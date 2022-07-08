# import argparse
from math import ceil
import os
import sys
from pathlib import Path

import cv2

from math import floor


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
    # List of all subdirectories in {ROOT}/data/raw
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


def extract_frame(input_path):
    # Read input video
    video = cv2.VideoCapture(f'{ROOT}/data/raw/{input_path}')

    # Used as counter variable
    count = 0
    # checks whether frames were extracted
    success = 1

    batch_size = 10001
    
    # Created output directory if it does not exist
    input_path = os.path.join(f'{ROOT}/data/frames/{input_path}')
    if not os.path.exists(input_path):
        os.makedirs(input_path)  

    while success:
        # Save each {bach_size} frames in a seprate folder
        for i in range(1, batch_size):
            # Extract frame each 1 second
            video.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
            success, image = video.read()

            # Create a new folder for next {bach_size} frames, if it does not exist
            batch_number = floor(count/batch_size)

            output_path = f'{input_path}/batch {batch_number}'

            if not os.path.exists(f'{output_path}'):
                os.mkdir(f'{output_path}')

            # Saves the frames with frame-count
            cv2.imwrite(f'{output_path}/{count}.jpg', image)
            print(f'Extract frame ({count})    {output_path}')
  
            count += 1



def main():
    # path = f'157820 - Leesburg PTMS & TTMS/CR 44 (117024)/15782017.mp4'
    # extract_frame(path)
    list = list_file(f'{ROOT}/data/raw/')
    for x in list:
        # print("x::::::::::::", x)
        extract_frame(x)
        

if __name__ == "__main__":
    main()