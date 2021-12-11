import discord
import firebase_admin
from discord.ext import commands
from commands.homework import Homework
from settings import *
from firebase_admin import db

class Done(commands.Cog, name="Done"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    #*หลังctxคือการเอาข้อมูลหลังคำสั่งมาทั้งหมดแล้วใส่ไปในตัวแปลattr
    async def done(self, ctx, *, attr = ""):
        hw = attr
        #ดึงข้อมูลมาจากDatabaseของFirebaseโดยทำการเรียกid discordของแต่ละคน
        homeworks = db.reference(f"/{ctx.author.id}/homeworks/").get()
        for key in homeworks:
            if homeworks[key]['name'] == hw:
                temp = key
        db.reference(f"/{ctx.author.id}/homeworks/{temp}/").delete()

        embed = discord.Embed(
        title="เย่ทำเสร็จแล้วว\n", description="งานที่เหลือ %d งาน" %(len(homeworks.keys())-1),
             color=colorframe
        )

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Done(bot))