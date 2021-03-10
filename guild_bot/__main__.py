import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")


@bot.command()
async def ping(ctx):
    await ctx.send("Hello World")


# Need to generate token
bot.run("")
