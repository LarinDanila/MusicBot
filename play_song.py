import asyncio
import os
import queue
import discord
import yt_dlp
from tokens import FFMPEG_PATH, SONG_PATH, SONG_PATH_NAME

#from bot_settings import Bot

#current_queue = queue.Queue()


'''@Bot.commands.command(name='play')
async def add_song_to_queue_and_play(ctx, song):
    global current_queue
    current_queue.put(song)
    await ctx.send(f'Queued: {song}')
    vc = discord.utils.get(Bot.commands.voice_clients, guild=ctx.guild)
    if not vc or not vc.is_playing:
        await play_from_queue(ctx)





'''


async def play_from_queue(ctx, current_queue):

    if not is_connected(ctx):
        voice_channel = ctx.author.voice.channel
        vc = await voice_channel.connect()
    else:
        vc = ctx.voice_client
    if not current_queue.empty():
        song = current_queue.get()
        download_song(song)
        # TODO: Добавить вывод трека
        vc.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH,
                                       source=SONG_PATH_NAME),
                after=lambda e: asyncio.run(play_from_queue(ctx, current_queue))
                )


def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


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
