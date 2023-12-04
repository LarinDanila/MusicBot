import asyncio

import discord
from discord.ext import commands

from cogs.Song import Song


async def setup(bot):
    await bot.add_cog(Song(bot))


class Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', self_bot=True, intents=intents)

    def __init__(self):
        asyncio.run(setup(self.bot))
