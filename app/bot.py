"""
Основной пакет с ботом
"""
import asyncio

import discord
from discord.ext import commands

from cogs.song import Song


async def setup(bot):
    """
    Method for setup cogs to bot
    :param bot: discord.Bot
    :return: None
    """
    await bot.add_cog(Song(bot))


class Bot:
    """
    Basic bot class wich contains all bot settings
    """
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', self_bot=True, intents=intents)

    def __init__(self):
        """
        Init class method
        """
        asyncio.run(setup(self.bot))
