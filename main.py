import discord
from discord.ext import commands
import os #ไปดึงpathไฟล์จากในเครื่อง
import firebase_admin
from firebase_admin import credentials, db
from settings import * #เอาข้อมูลมาจากไฟล์setting แล้วเอาข้อมูลอะไรมาบ้าง 

cred = credentials.Certificate(firebase_settings)
firebase_admin.initialize_app(cred, {
    'databaseURL': database_URL
})

bot = commands.Bot(command_prefix=prefix, help_command=None) #คือไอ้โค้ดปกติตรงนี้มันจะมีcommandให้เราอยู่แล้ว แต่เราต้องการสร้างcommandเอง เราเลยตั้งให้มันเป็นnone
@bot.event
async def on_ready():
    print(f"We Have Logged In As {bot.user}") #stringformat
    for file in os.listdir("commands"):
        if ".py" in file:
            file = file.split(".py")[0] #ต้องการแค่ชื่อไฟล์เฉยๆ
            bot.load_extension(f"commands.{file}") #บอทจะไปโหลดentensionจากไฟล์commands
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith(prefix): #เช็คว่ามันเริ่มต้นprefixที่เราสร้างไว้หรือเปล่า
        await bot.process_commands(message)


















bot.run(token)

