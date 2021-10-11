# 897087395177054278
# ODk3MDg3Mzk1MTc3MDU0Mjc4.YWQjvg.1_Jef0zy6GgGsjC7J1lEGbwvtTI
# 534723950656
import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f"Link start!!! {client.user}")


@client.event
async def on_message(message):
    if message.content == "!homework":
        print(message.channel)
        await message.channel.send('ยังไม่ได้ทำ')
    elif message.content == "!logout":
        await client.logout()


client.run('ODk3MDg3Mzk1MTc3MDU0Mjc4.YWQjvg.1_Jef0zy6GgGsjC7J1lEGbwvtTI')
