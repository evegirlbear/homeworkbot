import discord
from discord.ext import commands
from settings import *

class Help(commands.Cog, name="Help"):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
        title="ปิ๊ปๆสวัสดีจ้า\n", description="นี่คือคำสั่งเบื้องต้นของเราน้า\n",
        
             color=colorframe
        
         )
        embed.add_field(name="Prefix :",value="```pip!```", inline=False)
        embed.add_field(name="ตัวอย่างการพิมพ์คำสั่ง :",value="```pip!hi, pip!author, pip!homework\n\
pip!add PSITproject ส่งงานfinal 15/12/2021\n\
pip!done PSITproject```", inline=False)
        embed.add_field(name="คำสั่งทั่วไป  :",value="```pip!homework : โชว์listการบ้านที่เราได้เพิ่มไว้\n\
pip!add : ทำการเพิ่มการบ้านลงไปเล้ย\n\
pip!done : ทำการลบการบ้านที่เสร็จแล้วเย้\n\
pip!warning : เปิดแจ้งเตือนบอกการบ้านที่ใกล้กำหนดส่ง\n\
pip!motivation : ให้กำลังใจกันหน่อย ก็คนมันเหงา\n\
pip!logout : ออกจากระบบ เพื่อหนีความจริง```", inline=False )
        embed.set_thumbnail(url="https://www.it.kmitl.ac.th/wp-content/uploads/2017/12/it-logo.png") #URLภาพที่อยู่บนขวาของคำสั่ง help

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))