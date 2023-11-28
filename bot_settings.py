import discord
from discord.ext import commands


class Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', self_bot=True, intents=intents)
