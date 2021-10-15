import discord
from discord.ext import commands
from settings import colorframe

class Author(commands.Cog, name="Author"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def author(self, ctx):
        embed = discord.Embed(title="it's me", description="i'm student itkmitl", color=colorframe)


        await ctx.channel.send(embed=embed)





def setup(bot:commands.Bot):
    bot.add_cog(Author(bot))
