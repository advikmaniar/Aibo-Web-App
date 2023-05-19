import os
import time
import random
from PIL import Image
import cv2

# Get the path to the directory containing the python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths to image folders 
photo_folder = os.path.join(script_dir, "aibo_photos") # Replace this with the path to aibo's pictures folder
emoji_folder = os.path.join(script_dir, "emojis") # Replace this with the path to "emoji" folder
output_folder = os.path.join(script_dir, "output_pics")

# Loop to periodically search for new images
while True:
    # Get a list of all image files in the photo folder
    photo_files = [os.path.join(photo_folder, f) 
                   for f in os.listdir(photo_folder) if os.path.isfile(os.path.join(photo_folder, f))]
    print(photo_files)

    # Get a photo from photo_folder
    for photo_file in photo_files:
        # Open the photo file and a random emoji file
        photo = Image.open(photo_file)
        emoji_file = random.choice(os.listdir(emoji_folder))
        emoji = Image.open(os.path.join(emoji_folder, emoji_file))

        #---------------------------------Below part needs to be changed as per midjourney requirements-----------------------#
        # Resize the images before blending
        size = (640, 480)
        mode = "RGBA"
        # Photo
        photo = photo.resize(size)
        photo = photo.convert(mode)
        # Emoji
        emoji = emoji.resize(size)
        emoji = emoji.convert(mode)

        # Blend the two images together and convert to RGB mode
        mid_journey = Image.blend(photo, emoji, 0.8)
        mid_journey = mid_journey.convert("RGB")

        # Save the resulting image to the output folder
        output_file = os.path.join(output_folder, f"output_{time.time()}.jpg")
        mid_journey.save(output_file)

        # Display the resulting image
        img = cv2.imread(output_file)
        cv2.imshow("Mid Journey Image", img)
        cv2.waitKey(0)

        # Add a 5 sec delay between each picture (You can change it as per your requirement)
        time.sleep(5)