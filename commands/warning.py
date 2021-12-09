import discord
import firebase_admin
from discord.ext import commands, tasks
from firebase_admin import db
from settings import *
import asyncio
from datetime import date, datetime


class Warning(commands.Cog, name="Warning"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def warning(self, ctx):
        embed = discord.Embed(
            title="Warning !", description=f"เปิดระบบแจ้งเตือนแล้ว!!!",
            color=colorframe
        )
        await ctx.channel.send(embed=embed)
        while(True):
            homeworks = db.reference(f"/{ctx.author.id}/homeworks/").get()
            now = datetime.now()
            for key in homeworks:
                if int(homeworks[key]['deadline'][0:2]) == int(now.strftime("%d"))+1 and homeworks[key]['deadline'][3:5] == now.strftime("%m") and homeworks[key]['deadline'][6:10] == now.strftime("%Y"):
                    embed = discord.Embed(
                        title="%s !" % homeworks[key]['name'], description=f"ใกล้ครบกำหนดส่ง",
                        color=colorframe
                    )
                    await ctx.channel.send(embed=embed)
                elif int(homeworks[key]['deadline'][0:2]) == int(now.strftime("%d")) and homeworks[key]['deadline'][3:5] == now.strftime("%m") and homeworks[key]['deadline'][6:10] == now.strftime("%Y"):
                    embed = discord.Embed(
                        title="%s !!!" % homeworks[key]['name'], description=f"ถึงวันกำหนดส่งแล้ว",
                        color=colorframe
                    )
                    await ctx.channel.send(embed=embed)
            await asyncio.sleep(60)  # delay การแจ้งเตือน ใส่เลขเป็นวินาทีคิดว่าน่าจะใช้ที่ 3600


def setup(bot: commands.Bot):
    bot.add_cog(Warning(bot))
