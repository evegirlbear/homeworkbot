
import discord
from discord.ext import commands
from settings import *
from firebase_admin import db #คือการดึงคำสั่งจากfirebaseมาใช้


class Homework(commands.Cog, name="Homework"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def homework(self, ctx): #ctxคือข้อมูลของ"messages" จะบอกแมสเซจนี้ว่ามีไรบ้าง 
        #ดึงข้อมูลมาจากDatabaseของFirebaseโดยทำการเรียกid discordของแต่ละคน
        homeworks = db.reference(f"/{ctx.author.id}/homeworks/").get()
        embed = discord.Embed(
        title="ปิ๊ป ปิ๊ป การบ้านของเธอมีดังนี้จ้า\n", description="ท้อได้ แต่ห้ามถอยน้า เรียนจบไปด้วยกัน ฮึบ\n",
             color=colorframe
         ) 
        for key in homeworks:
          embed.add_field(name=f"{homeworks[key]['name']} :",value=f"```\n{homeworks[key]['description']}\n{homeworks[key]['deadline']}```", inline=False)
        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Homework(bot))