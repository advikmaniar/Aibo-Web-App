import cv2
import numpy as np

# Convert real-time video to bitmap information
cap = cv2.VideoCapture(1) # Read video input from camera 1 (Change to aibo's camera module)
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480)) # Save video in directory
bitmap_info = [] # Empty list to store bitmap info 

while True:
    ret, frame = cap.read() # Each frame captured is stored in variable "frame"
    if not ret:
        break
    out.write(frame)
    frame_array = np.array(frame) # Convert frame to numpy array (easier manipulation)
    if frame_array.ndim != 3: # If frame is not a RGB image, it breaks the loop
        break
    each_frame_pixel_info = [] # Empty list to store pixel information of each frame
    pixel_info = frame_array[100, 200]
    print(pixel_info) # Testing
    for i in range(frame_array.shape[0]):
        row_pixel_info = []
        for j in range(frame_array.shape[1]):
            row_pixel_info.append(frame_array[i, j])
        each_frame_pixel_info.append(row_pixel_info)
    bitmap_info.append(each_frame_pixel_info)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

bitmap_info = np.array(bitmap_info, dtype=np.uint8)
n_frames, height, width = bitmap_info.shape[:3]

bitmap_info_R = bitmap_info[:,:,0].ravel()
bitmap_info_G = bitmap_info[:,:,1].ravel()
bitmap_info_B = bitmap_info[:,:,2].ravel()

# Save the data in a CSV file with columns as R, G, B values 
data = np.column_stack((bitmap_info_R, bitmap_info_G, bitmap_info_B))
np.savetxt("bitmap_info.csv", data, delimiter=",", fmt="%d")





