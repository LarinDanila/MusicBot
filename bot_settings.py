import asyncio
import queue

import discord
from discord.ext import commands
from play_song import play_from_queue


class Song(commands.Cog):
    current_queue = queue.Queue()

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def add_song_to_queue_and_play(self, ctx: commands.Context, song: str):
        self.current_queue.put(song)
        await ctx.send(f'Queued: {song}')
        vc = discord.utils.get(Bot.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_playing:
            await play_from_queue(ctx, self.current_queue)


class Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', self_bot=True, intents=intents)

    def __init__(self):
        asyncio.run(self.setup(self.bot))

    async def setup(self, bot):
        await bot.add_cog(Song(bot))
