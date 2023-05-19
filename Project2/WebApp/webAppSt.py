import sys
import streamlit as st
import os
import time
from PIL import Image
import random
import numpy as np


st.markdown("""
<style>
    .title {
        font-size: 50px;
        font-family: 'Georgia', Tahoma, Geneva, Verdana, sans-serif;
        color: white;
        text-align: center;
        margin-bottom: 20px;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Image Gallery</p>', unsafe_allow_html=True)

# Define paths to image folders 
photo_folder = "C:/Users/advik/Data/MS/New_York_Institute_of_Technology/RA_SoAD/Project2/aibo_photos" # Replace this with the path to aibo's pictures folder
emoji_folder =  "C:/Users/advik/Data/MS/New_York_Institute_of_Technology/RA_SoAD/Project2/emojis"# Replace this with the path to "emoji" folder
output_folder = 'C:/Users/advik/Data/MS/New_York_Institute_of_Technology/RA_SoAD/Project2/WebApp/output_pics'
captions = ["WOW","WOAH","AMAZING","GREAT","AWESOME","INCREDIBLE"]

# @st.cache(allow_output_mutation=True)
def get_latest_image(output_folder):
    # Get a list of file names in the source folder
    file_names = os.listdir(output_folder)
    if not file_names:
        # Return None if the directory is empty
        return None
    # Sort the file names based on the modification time
    file_names.sort(key=lambda x: os.path.getctime(os.path.join(output_folder, x)), reverse=True)
    # Return the latest file name
    return file_names[0]

def main():
    # Initialize the latest file name to None
    latest_filename = None
    running = True

    while running:
        # Get a list of all image files in the photo folder
        photo_files = [os.path.join(photo_folder, f) 
                    for f in os.listdir(photo_folder) if os.path.isfile(os.path.join(photo_folder, f))]
        print(photo_files)

        # Get the latest file in the photo folder
        latest_file = max(photo_files, key=os.path.getctime)

        # Check if the latest file is different from the previous one
        if latest_file != latest_filename:
            # Update the latest file name
            latest_filename = latest_file

            # Open the photo file and a random emoji file
            photo = Image.open(latest_filename)
            emoji_file = random.choice(os.listdir(emoji_folder))
            emoji = Image.open(os.path.join(emoji_folder, emoji_file))

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

            # Display the latest image on the dashboard
            st.image(mid_journey, caption=random.choice(captions))


if __name__ == '__main__':
    main()


