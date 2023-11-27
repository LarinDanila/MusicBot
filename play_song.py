import discord
from discord.ext import commands
from bot_settings import Bot
import queue
from collections import deque
import yt_dlp
import os
import asyncio
from tokens import FFMPEG_PATH, SONG_PATH, SONG_PATH_NAME


current_queue = queue.Queue()


@Bot.bot.command(name='play')
async def add_song_to_queue_and_play(ctx, song):
    global current_queue
    current_queue.put(song)
    await ctx.send(f'Queued: {song}')
    vc = discord.utils.get(Bot.bot.voice_clients, guild=ctx.guild)
    if not vc or not vc.is_playing:
        await play_from_queue(ctx)
        


async def play_from_queue(ctx, vc=None):
    global current_queue
    voice_channel = ctx.author.voice.channel
    print(type(ctx.author.voice.channel))
    # print(f'current_queue: {current_queue.}')
    if voice_channel != None:
        if not current_queue.empty():
            download_song(current_queue.get())
            # channel = voice_channel.name
            if not vc:
                vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, 
                                        source=SONG_PATH_NAME), 
                                        after=lambda e: asyncio.run(play_from_queue(ctx, vc))
                                        )


def download_song(song_url):
    if os.path.isfile('song.mp3'):
        os.remove('song.mp3')
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': SONG_PATH
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_url])
