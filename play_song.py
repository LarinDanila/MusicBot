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


@Bot.commands.command(name='skip')
async def skip_playing_song(ctx):
    vc = discord.utils.get(Bot.commands.voice_clients, guild=ctx.guild)
    if not vc or not vc.is_playing:
        await ctx.send(f'Nothing playing')
    else:
        if not is_connected(ctx):
            await ctx.send(f'Bot not in voice channel')
        else:
            vc = ctx.voice_client
        vc.skip()


@Bot.commands.command(name='pause')
async def pause_playing_song(ctx):
    vc = discord.utils.get(Bot.commands.voice_clients, guild=ctx.guild)
    if not vc or not vc.is_playing:
        await ctx.send(f'Nothing playing')
    else:
        if not is_connected(ctx):
            await ctx.send(f'Bot not in voice channel')
        else:
            vc = ctx.voice_client
        vc.pause()


@Bot.commands.command(name='resume')
async def resume_playing_song(ctx):
    vc = discord.utils.get(Bot.commands.voice_clients, guild=ctx.guild)
    if not vc or not vc.is_paused:
        await ctx.send(f'Nothing on pause')
    else:
        if not is_connected(ctx):
            await ctx.send(f'Bot not in voice channel')
        else:
            vc = ctx.voice_client
        vc.resume()
'''


async def play_from_queue(ctx, current_queue):
    if not is_connected(ctx):
        voice_channel = ctx.author.voice.channel
        vc = await voice_channel.connect()
    else:
        vc = ctx.voice_client
    if not current_queue.empty():
        download_song(current_queue.get())
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
