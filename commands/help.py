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
        embed.add_field(name="ตัวอย่างการพิมพ์คำสั่ง :",value="```pip!author, pip!homework```", inline=False)
        embed.add_field(name="คำสั่งทั่วไป  :",value="```pip!add : ทำการเพิ่มการบ้านลงไปเล้ย\n\
pip!homework : โชว์listการบ้านที่เราได้เพิ่มไว้\n\
pip!deadline : แสดงงานที่ต้องใกล้ส่งภายใน3วัน!!!```", inline=False )

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))