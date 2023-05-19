import cv2
import numpy as np
import pandas as pd

# Read CSV file and obtain flattened R, G, B values
data = pd.read_csv('bitmap_info.csv', header=None)
bitmap_info_R = data.iloc[:, 0].values
bitmap_info_G = data.iloc[:, 1].values
bitmap_info_B = data.iloc[:, 2].values

# Reshape flattened arrays back to original dimensions of frames
n_frames = len(bitmap_info_R) // (640*480)
height = 480
width = 640
R = bitmap_info_R.reshape((n_frames, height, width))
G = bitmap_info_G.reshape((n_frames, height, width))
B = bitmap_info_B.reshape((n_frames, height, width))

# Stack R, G, and B arrays together to obtain original RGB arrays for each frame
bitmap_info = np.stack((R, G, B), axis=-1)

# Convert bitmap_info back to uint8 type
bitmap_info = bitmap_info.astype(np.uint8)

# Combine RGB arrays into 3D array representing video frames
out = cv2.VideoWriter('reproduced.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (width, height))
for frame in bitmap_info:
    out.write(frame)

out.release()


