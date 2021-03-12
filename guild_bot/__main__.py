import discord
import logging
import os
import sys
from discord.ext import commands

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)
logger.info("Starting suggestion_bot")

TOKEN = os.getenv('API_TOKEN')
if TOKEN == None:
    sys.exit("Environment variable API_TOKEN must be supplied")

CHANNEL = os.getenv('SUGGESTION_CHANNEL')
if CHANNEL == None:
    sys.exit("Environment variable SUGGESTION_CHANNEL must be supplied")

bot = commands.Bot(command_prefix="!")


@bot.command(help="Send anonymous suggestion")
async def suggest(ctx):
    try:
        channel_id = int(CHANNEL)
    except Exception as e:
        raise ValueError("SUGGESTION_CHANNEL environment variable must be an int!") from e
    channel = bot.get_channel(channel_id)
    msg = ctx.message.content.replace("!suggest", "")
    await channel.send(msg)

# Need to generate token
bot.run(TOKEN)
