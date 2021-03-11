import discord
import os
import sys
from discord.ext import commands

TOKEN = os.getenv('API_TOKEN')
if TOKEN == None:
    sys.exit("Environment variable API_TOKEN must be supplied")

CHANNEL = os.getenv('SUGGESTION_CHANNEL')
if CHANNEL == None:
    sys.exit("Environment variable SUGGESTION_CHANNEL must be supplied")

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    await ctx.send("Hello World")

@bot.command()
async def suggest(ctx):
    channel = bot.get_channel(int(CHANNEL))
    msg = ctx.message.content
    await channel.send(msg)

# Need to generate token
bot.run(TOKEN)
