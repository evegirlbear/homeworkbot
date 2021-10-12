
import discord
import os
import json

if os.path.exists(os.getcwd() + "../config.json"):
    with open("../config.json") as f:
        configData = json.load(f)
        token = configData["Token"]
else:
    token = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(token)