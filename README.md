# Aibo-Web-App

**Project 1:**
- It includes a python script (**_project_1.py_**) to convert the video information captured from Aibo's camera to bitmap information in realtime (saved in a csv file **_bitmap_info.csv_**) for further use.
- Currently the input is set to the default webcam in the system. Change it to the desired video input (For example to Aibo's video output)

<hr>

**Project 2:**
- This is the main project to blend 2 images (one from Aibo's realtime captured image and other a random image from the "emojis" folder) using Midjourney Bot in discord and display the result on the Web Application dashboard.
- There are 2 main scripts in the folder: <br>
1. `discordBot.py`
2. `webAppSt.py`

The following variables need to be changed appropriately before use:
- Change the folder paths in each of the scripts above to the appropriate directories where the images are located. (line 26-28)
- In the `discordBot.py` file, change the TOKEN and CHANNEL_ID by generating your own API token from discord developers website (the token in the code will not work)

**Challenges Faced:**
- Invoking the `/blend` command automatically through the created Discord bot in the Midjourney Bot channel. `/blend` is predefined command for the Midjourney Bot and not for the Discord Bot, hence invoking it would require the access of Midjourney API (which does not exist)

**Work Pending:**
- Link Aibo's backend API to the **_photo_folder_** variable in the script to directly fetch the images when Aibo captures a picture. Currently the photo_folder is pointing to a directory on the system where images are stored beforehand.
- Merge the two scripts together in a single file which basically do the following tasks automatically:
    1. Get captured image from Aibo's API automatically. (Not done)
    2. Select a random picture from the "emoji" folder. (Done)
    3. Send these 2 images to the Midjourney bot channel in Discord and invoke the `/blend` command on them. (Not done)
    4. Display the blended image on the Web Application developed using python and streamlit. (Done)


 > RUN THE FILE WITH COMMAND  _**streamlit run webAppSt.py**_ in the terminal.
