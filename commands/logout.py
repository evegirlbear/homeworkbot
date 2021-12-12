import discord
from discord.ext import commands
from settings import *
import random

list_logout = ["แล้วพบกันใหม่ เมื่อชาติต้องการ", "มีพบ ก็ต้องมีจาก แล้วเจอกันใหม่", "การบ้านใหม่ จะกลับมาในไม่ช้า"]

class Logout(commands.Cog, name="Logout"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def logout(self, ctx):
        embed = discord.Embed(
        title="ลาก่อนชาวโลก T______T", description=f"```{random.choice(list_logout)}```",
             color=colorframe
         )

        await ctx.channel.send(embed=embed)
        await self.bot.logout()

def setup(bot: commands.Bot):
    bot.add_cog(Logout(bot))