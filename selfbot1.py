import discord
from discord.ext import commands

bot = commands.Bot("masukin prefix/put prefix", self_bot=True)

@bot.event
async def on_ready():
    print("Self Bot Ready")#console logs nya kalo dia nyala #console logs if the selfbot on

@bot.command()
async def test(ctx):
    await ctx.send("Gay people like kesV")

bot.run("token bot/token bot lu anjg", bot=False)#selesai