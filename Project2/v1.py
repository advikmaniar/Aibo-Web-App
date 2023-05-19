import os
import time
import random
from PIL import Image
import cv2
import discord
from discord.ext import commands
import os

# For discord
TOKEN = 'MTA5ODAzMzk1OTQzMjA5Nzg3Mw.G7WZLK.JeSjhYNf-Xbw_bT8xi2h-Kx09oWlJThp1z70ok'
CHANNEL_ID_ME = '1098846685536473199'
CHANNEL_ID_MJ = '1098841631265919089'

# Get the path to the directory containing the python script
script_dir = os.path.dirname(os.path.relpath(__file__))

# Define paths to image folders 
photo_folder = os.path.join(script_dir, "aibo_photos") # Replace this with the path to aibo's pictures folder
emoji_folder = os.path.join(script_dir, "emojis") # Replace this with the path to "emoji" folder
output_folder = os.path.join(script_dir, "output_pics")


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

    





        