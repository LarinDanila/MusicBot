"""
All song commands for bot in discord.cogs
"""
import queue

import discord
from discord.ext import commands

from app.play_song import play_from_queue, is_connected


class Song(commands.Cog):
    """
    Class for processing bot command
    """
    current_queue = queue.Queue()

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def add_song_to_queue_and_play(
            self,
            ctx: commands.Context,
            song=None
    ):
        """
        Method for
        :param ctx: discord context
        :param song: string - now url to song
        :return: None
        """
        if song is not None:
            self.current_queue.put(song)
            await ctx.send(f'Queued: {song}')
        vc = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_playing():
            await play_from_queue(ctx, self.current_queue)

    @commands.command(name='skip')
    async def skip_playing_song(self, ctx: commands.Context):
        """

        :param ctx:
        :return:
        """
        vc = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_playing:
            await ctx.send('Nothing playing')
        else:
            if not is_connected(ctx):
                await ctx.send('Bot not in voice channel')
            else:
                vc = ctx.voice_client
            vc.stop()
            await self.add_song_to_queue_and_play(ctx)

    @commands.command(name='pause')
    async def pause_playing_song(self, ctx: commands.Context):
        """

        :param ctx:
        :return:
        """
        vc = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_playing:
            await ctx.send('Nothing playing')
        else:
            if not is_connected(ctx):
                await ctx.send('Bot not in voice channel')
            else:
                vc = ctx.voice_client
            vc.pause()

    @commands.command(name='resume')
    async def resume_playing_song(self, ctx: commands.Context):
        """

        :param ctx:
        :return:
        """
        vc = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_paused:
            await ctx.send('Nothing on pause')
        else:
            if not is_connected(ctx):
                await ctx.send('Bot not in voice channel')
            else:
                vc = ctx.voice_client
            vc.resume()
