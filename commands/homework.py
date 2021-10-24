import discord
from discord.ext import commands
from settings import *

list_homework_itkmitl = [
  {
    "name": "ITF",
    "description": "การบ้านทำ Assignment",
  },
  {
    "name": "ICS",
    "description": "การบ้านทำ Assignment Week 5",
  },
  {
    "name": "PSIT",
    "description": "ทำโจทย์หน้า 1-5",
  },
  {
    "name": "Gen B",
    "description": "สอบ 25",
  }
]
class Homework(commands.Cog, name="Homework"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def homework(self, ctx):
        embed = discord.Embed(
        title="เกิด แก่ เจ็บ ทำการบ้าน เย้เย้\n", description="ห้ามป่วย ห้ามตุย ห้ามเอฟ เฮ้!\n",
             color=colorframe
         )
        for subject in list_homework_itkmitl:
            embed.add_field(name= f"{subject['name']} มีการบ้านดังนี้ T_T!" ,value= subject["description"], inline=False)
        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Homework(bot))