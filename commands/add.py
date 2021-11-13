import discord
import firebase_admin
from discord.ext import commands
from settings import *
from firebase_admin import db

class Add(commands.Cog, name="Add"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    #*หลังctxคือการเอาข้อมูลหลังคำสั่งมาทั้งหมดแล้วใส่ไปในตัวแปลattr
    async def add(self, ctx, *, attr = ""):
        hw = attr.split()
        #ดึงข้อมูลมาจากDatabaseของFirebaseโดยทำการเรียกid discordของแต่ละคน
        addhw = db.reference(f"/{ctx.author.id}/homeworks/")      
        #เมื่อมีการดึงข้อมูลก็ให้firebaseอัพเดตข้อมูลตลอดเวลา
        #ตรงนี้มันคือการอัพเดพข้อมูลแบบเดี่ยว
        # addhw.update({
        #     "homeworks" : {
        #          "name": hw[0],
        #          "description": hw[1],
        #          "deadline": hw[2]
        #     }
        # })
        
        #การอัพเดตข้อมูลแบบเป็นลิสต์ เป็นการส่งข้อมูลขึ้นไป
        addhw.push({
            "name": hw[0],
            "description": hw[1],
            "deadline": hw[2]
        })
        
        embed = discord.Embed(
        title="เค้าเพิ่มการบ้านให้แล้วน้า\n",  description="ดูรายชื่อการบ้าน pip!homework โลดดด",
             color=colorframe
         )

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Add(bot))