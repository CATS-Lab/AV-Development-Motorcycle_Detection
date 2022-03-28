import cv2
from torch import le

def extract_frame(video_path):
    video = cv2.VideoCapture(video_path)

    success = True
    count =1

    while success:
        success, frame = video.read()
        output = '../data/Extracted Frames/A1A SB North of Edgewater Lakes Blvd/Cam 736 - Facing North/vi_0005_20220309_134449.mp4/' + str(count) + '.jpg'
        if success == True:
            cv2.imwrite(output, frame)
            # print('Frame {} Extracted Successfully'.format(count))
            count = count + 1
        else:
            break


path = "../data/153940 - Daytona Collections/A1A SB North of Edgewater Lakes Blvd/Cam 736 - Facing North/vi_0005_20220309_134449.mp4"
path_list = ["../data/153940 - Daytona Collections/US Hwy 1 NB South of Bunnell Gas Mart/Cam 753 - facing North",
             "../data/153940 - Daytona Collections/US Hwy 1 NB South of Bunnell Gas Mart/Cam 737 - facing South",
             "../data/153940 - Daytona Collections/A1A SB North of Edgewater Lakes Blvd/Cam 736 - Facing North",
             "../data/153940 - Daytona Collections/A1A SB North of Edgewater Lakes Blvd/Cam 745 - Facing North",
             "../data/153940 - Daytona Collections/Video Only Locations/S Williamson @ Bellvue",
             "../data/153940 - Daytona Collections/Video Only Locations/Tomoka @ Bellvue",
             "../data/153940 - Daytona Collections/Hwy 92 EB West of Lanscam Ln/Cam 734 - don't use",
             "../data/153940 - Daytona Collections/Hwy 92 EB West of Lanscam Ln/Cam 505 - facing Northeast"]
extract_frame(path)
# tmp = "../data/153940 - Daytona Collections"
# print(tmp[36])