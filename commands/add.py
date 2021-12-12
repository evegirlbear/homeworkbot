import discord
import firebase_admin
from discord.ext import commands
from settings import *
from datetime import date, datetime
from firebase_admin import db

class Add(commands.Cog, name="Add"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    #*หลังctxคือการเอาข้อมูลหลังคำสั่งมาทั้งหมดแล้วใส่ไปในตัวแปลattr
    async def add(self, ctx, *, attr = ""):
        hw = attr.split()
        now = datetime.now()
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
        if len(hw) != 3 or len(hw[2]) != 10 or int(hw[2][0:2]) > 31 or int(hw[2][3:5]) > 12 or\
            (int(hw[2][0:2]) < int(now.strftime("%d")) and\
            int(hw[2][3:5]) <= int(now.strftime("%m")) and\
            int(hw[2][6:10]) <= int(now.strftime("%Y"))):
            embed = discord.Embed(
            title="ปิ๊ป ข้อมูลไม่ถูกต้อง(ห้ามย้อนอดีต)\n",
                color=colorframe
            )
            embed.add_field(name="ตัวอย่างการใช้ pip!add :",value="```pip!add ชื่องาน รายละเอียด 01/12/2029```", inline=False)
            await ctx.channel.send(embed=embed)
        else:
            addhw.push({
                "name": hw[0],
                "description": hw[1],
                "deadline": hw[2]
            })
            time = 0
            homeworks = db.reference(f"/{ctx.author.id}/homeworks/").get()
            for key in homeworks:
                if homeworks[key]['name'] == hw[0]:
                    time += 1
                    temp = key
            #เช็กรูปแบบการใส่ข้อมูล
            if time > 1:
                db.reference(f"/{ctx.author.id}/homeworks/{temp}/").delete()
                embed = discord.Embed(
                title="ปิ๊ป ชื่องานซ้ำ\n", description="-ลองเปลี่ยนเป็นชื่ออื่นน้าา-",
                    color=colorframe
                )
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                title="เค้าเพิ่มการบ้านให้แล้วน้า\n",  description="ดูรายชื่อการบ้าน pip!homework โลดดด",
                    color=colorframe
                )
                await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Add(bot))