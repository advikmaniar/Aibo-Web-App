import discord
import requests
from io import BytesIO
from PIL import Image

# Discord bot
TOKEN = 'MTA5ODAzMzk1OTQzMjA5Nzg3Mw.G7WZLK.JeSjhYNf-Xbw_bT8xi2h-Kx09oWlJThp1z70ok'
IMAGE_PATH_1 = 'Project2/emojis/Ghost Emoji [Download iPhone Emojis].png'
IMAGE_PATH_2 = 'Project2/emojis/Eye Roll Emoji in PNG [Free Download IOS Emojis].png'
CHANNEL_ID_MJ = '1098841631265919089'

client = discord.Client(command_prefix='/', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/blend'):
        image_paths = message.content.split()[1:] # Get the image paths from the command
        if len(image_paths) != 2:
            await message.channel.send('Invalid command. Please provide two image paths.')
            return

        # Load the images using PIL
        image1 = Image.open(IMAGE_PATH_1)
        image2 = Image.open(IMAGE_PATH_2)

        # Convert the images to bytes
        image1_bytes = image1.tobytes()
        image2_bytes = image2.tobytes()

        # Send the request to the MidJourney bot
        headers = {
            'Authorization': 'Bot YOUR_BOT_TOKEN_HERE',
        }

        data = {
            'content': '/blend',
            'channel_id': message.channel.id,
            'files': [
                ('image1.png', BytesIO(image1_bytes)),
                ('image2.png', BytesIO(image2_bytes))
            ]
        }

        response = requests.post('https://discord.com/api/v9/channels/{}/messages'.format(CHANNEL_ID_MJ), headers=headers, data=data)

        if response.status_code == 200:
            await message.channel.send('Command sent successfully.')
        else:
            await message.channel.send('An error occurred while sending the command.')
        
client.run(TOKEN)
