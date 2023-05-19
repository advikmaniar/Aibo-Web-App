import asyncio
from io import BytesIO
import discord
from discord.ext import commands
import os
from PIL import Image
import pyautogui as pg

# Discord bot
TOKEN = 'MTA5ODAzMzk1OTQzMjA5Nzg3Mw.G7WZLK.JeSjhYNf-Xbw_bT8xi2h-Kx09oWlJThp1z70ok'

CHANNEL_ID_ME = '1098846685536473199'
CHANNEL_ID_MJ = '1098841631265919089'
CHANNEL_ID = '1008571067398369291'

APPLICATION_ID = '1098033959432097873'
COMMAND_ID = '1062880104792997970'

IMAGE_PATH_1 = 'Project2/emojis/Ghost Emoji [Download iPhone Emojis].png'
IMAGE_PATH_2 = 'Project2/emojis/Eye Roll Emoji in PNG [Free Download IOS Emojis].png'

# Get the path to the directory containing the python script
SCRIPT_DIR = os.path.dirname(os.path.relpath(__file__))

# Define paths to image folders 
photo_folder = "C:/Users/advik/Data/MS/New_York_Institute_of_Technology/RA_SoAD/Project2/aibo_photos" # Replace this with the path to aibo's pictures folder
emoji_folder =  "C:/Users/advik/Data/MS/New_York_Institute_of_Technology/RA_SoAD/Project2/emojis"# Replace this with the path to "emoji" folder
output_folder = 'C:/Users/advik/Data/MS/New_York_Institute_of_Technology/RA_SoAD/Project2/WebApp/output_pics'

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# Define function to send pictures to discord channel
@client.command()
async def send_message(channel_id):
    channel = await client.fetch_channel(channel_id)
    with open(IMAGE_PATH_1, 'rb') as f:
        picture1 = discord.File(f)
    with open(IMAGE_PATH_2, 'rb') as f:
        picture2 = discord.File(f)

    # await ctx.invoke(client.get_command('trigger'), command_id=COMMAND_ID, application_id=APPLICATION_ID, image1=image1_bytes, image2=image2_bytes)
    # await channel.send(f"/blend{picture1}{picture2}")
    await channel.send(pg.write("/blend"))

    print('Message sent')
    await asyncio.sleep(1)
    await client.close()

        
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    channel = await client.fetch_channel(CHANNEL_ID_MJ)
    print(f'Fetched channel: {channel.name} ({channel.id})')

    await send_message(CHANNEL_ID_MJ)
    # await client.get_command('blend').invoke(image1=IMAGE_PATH_1, image2=IMAGE_PATH_2, channel_id=CHANNEL_ID_MJ)

    print("on_ready executed")

@client.event
async def on_error(error, *args, **kwargs):
    print(error)

# Define main and run Discord Bot
async def main():
    try:
        async with client:
            print("Main function executed")
            await client.start(TOKEN)
    finally:
        await client.close()
        await asyncio.sleep(0.5)


# Run main function
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        asyncio.run(asyncio.sleep(0))
        print("Program Ended!")
