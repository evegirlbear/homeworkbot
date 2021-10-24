import discord
import firebase_admin
from discord.ext import commands
from settings import *
from firebase_admin import db

class Add(commands.Cog, name="Add"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def add(self, ctx, *, attr = ""):
        hw = attr.split()
        ref = db.reference(f"/{ctx.author.id}/")
        ref.update({
            1 : {
                 "name": hw[0],
                 "description": hw[1],
                 "deadline": hw[2]
            }
        })
        embed = discord.Embed(
        title="เพิ่มจ้า",
             color=colorframe
         )

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Add(bot))