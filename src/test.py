# import torch

# # Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# # Images
# img = '/home/hoorad/Desktop/VMT/data/Screenshot from 2022-03-24 12-32-55.png'  # or file, Path, PIL, OpenCV, numpy, list

# # Inference
# results = model(img)

# # Results
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
# results.save('/home/hoorad/Desktop/VMT/results')




# import numpy as np
# import pandas as pd

# def train_validate_test_split(df, train_percent=.6, validate_percent=.2, seed=None):
#     np.random.seed(seed)
#     perm = np.random.permutation(df.index)
#     m = len(df.index)
#     train_end = int(train_percent * m)
#     validate_end = int(validate_percent * m) + train_end
#     train = df.iloc[perm[:train_end]]
#     validate = df.iloc[perm[train_end:validate_end]]
#     test = df.iloc[perm[validate_end:]]
#     return train, validate, test

import splitfolders
dir = "/home/hoorad/Desktop/VMT/data/Extracted Frames/A1A SB North of Edgewater Lakes Blvd/Cam 736 - Facing North/vi_0005_20220309_134449.mp4"
# dir = "../data/Extracted\ Frames/A1A\ SB\ North\ of\ Edgewater\ Lakes\ Blvd/Cam\ 736\ -\ Facing\ North/vi_0005_20220309_134449.mp4/"
splitfolders.ratio(dir, output="output", seed=1337, ratio=(.8, 0.1,0.1))




# # import OS module
# import os
 
# # Get the list of all files and directories
# path = "../data/153940 - Daytona Collections/"
# dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# # prints all files
# # print(dir_list)

# for sub_dir in dir_list:
#     sub_path = path + sub_dir

# import os
# dir = "../data/153940 - Daytona Collections"
# dir_list = [x[0] for x in os.walk(dir)]
# # dir_list = [os.path.join(dir, o) for o in os.listdir(dir) if os.path.isdir(os.path.join(dir,o))]
# for sub_dir in dir_list:
#     print(sub_dir)