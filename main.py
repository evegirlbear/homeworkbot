
import discord
import json
import os

client = discord.Client()

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
        token = configData["Token"]
        prefix = configData["Prefix"]
else:
    token = ""
    prefix = "!"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    msg = message.content.lower().split(prefix)[1].strip().split(" ")
    if msg[0] == "sunwoo":
        await message.channel.send('loveeve')
    elif msg[0] == "theboyz":
        await message.channel.send('number1 gen4')


client.run(token)