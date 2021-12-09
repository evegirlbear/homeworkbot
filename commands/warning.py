import discord
from discord.ext import tasks
import firebase_admin
from discord.ext import commands
from firebase_admin import db
from settings import *

class Warning(commands.Cog, name="Warning"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @tasks.loop(seconds = 10) 
    async def warning(): #ยังทำไม่สำเร็จไม่รู้ว่าจะเลือกchannelที่แจ้งเตือนchannelไหน"warning()""
        embed = discord.Embed(
        title="Warning!", description=f"แจ้งเตือน",
             color=colorframe
        )
        await channel.send(embed=embed)      #ยังทำไม่สำเร็จไม่รู้ว่าจะเลือกchannelที่แจ้งเตือนchannelไหน


    warning.start()

def setup(bot: commands.Bot):
    bot.add_cog(Warning(bot))
       


