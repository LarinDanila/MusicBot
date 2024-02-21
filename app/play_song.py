"""
Methods for processing tracks url
"""
import asyncio
import os
import discord
import yt_dlp
from tokens import FFMPEG_PATH, SONG_PATH, SONG_PATH_NAME


def is_connected(ctx):
    """
    Methods for check is discord bot connected to voice chat
    :param ctx: discord context
    :return: is bot connected to voice chat
    """
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


def download_song(song_url):
    """
    Method for download track from YouTube
    :param song_url: url to track
    :return: None
    """
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
