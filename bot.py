import discord
import requests

# Replace this with your Mattermost webhook URL
webhook_url = r"https://mattermost.ecs.vuw.ac.nz/hooks/wakgf3geyidquyekae1aik969h"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
guild = discord.Guild

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} ({client.user.id})")
    print(discord.Intents.message_content in discord.Intents.default().all())

@client.event
async def on_message(message):
    channelIDs = 1084593366911701042

    #Check if the message was sent in the specific channel you want to monitor
    if message.channel.id == channelIDs:
        # Construct the payload for the Mattermost webhook
        payload = {
            "username": message.author.display_name + " - Discord",
            "text": message.content,
        }
        # Send the payload to the Mattermost webhook using a POST request
        response = requests.post(webhook_url, json=payload)
        # Print the response status code for debugging purposes
        print(response.status_code)

# Replace this with your Discord bot token

client.run("MTA5Mjk4MzkzMjgxMjc5MTgwOA.Ga2FAz.9nxyAEazUmuKLaKh7EREq1A2P4ZMugNZ6CmtoU")
