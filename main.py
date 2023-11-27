import discord
from discord.ext import commands
from tokens import TOKEN
import asyncio
from bot_settings import Bot
import play_song


Bot.bot.run(token=TOKEN)
