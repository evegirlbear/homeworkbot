import discord
from discord.ext import commands
from settings import *
import random

list_hihi = ["วันนี้เพื่อนๆเคลียร์งานค้างกันหรือยังเอ่ย ?-?", "ฮั่นแน่ ยังอีก ยังเล่นอยู่อีก ไปทำการบ้าน!!", "เคลียร์การบ้านวันนี้สบายวันหน้า"]

class Hi(commands.Cog, name="Hi"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def hi(self, ctx):
        embed = discord.Embed(
        title="สวัสดีชาวโลก >______<", description=f"```{random.choice(list_hihi)}```",
             color=colorframe
         )

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Hi(bot))