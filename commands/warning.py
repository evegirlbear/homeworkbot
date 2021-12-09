import discord
import firebase_admin
from discord.ext import commands, tasks
from firebase_admin import db
from settings import *
import asyncio


class Warning(commands.Cog, name="Warning"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def warning(self, ctx):
        embed = discord.Embed(
            title="Warning!", description=f"เปิดระบบแจ้งเตือนแล้ว!!!",
            color=colorframe
        )
        await ctx.channel.send(embed=embed)
        while(True):
            # ทำloopตรวจcheckเวลาแล้วเหลือทำเงื่อนไขเพื่อแจ้งเตือน
            await asyncio.sleep(1)


def setup(bot: commands.Bot):
    bot.add_cog(Warning(bot))
