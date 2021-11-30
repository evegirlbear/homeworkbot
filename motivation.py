import discord
from discord.ext import commands
from settings import *
import random

txt_motivation = ["เหนื่อยละซิ๊ พักก่อนก็ได้~~", "ไหวรึเปล่าา สู้ๆน้าาาา", "อย่าเครียดมากน้าา เป็นห่วงง"]

class Motivation(commands.Cog, name="motivation"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def motivation(self, ctx):
        embed = discord.Embed(
        title="ว่าไงง~~~~", description=f"```{random.choice(txt_motivation)}```",
             color=colorframe
         )

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Motivation(bot))