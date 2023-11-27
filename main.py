import discord
from discord.ext import commands
from tokens import TOKEN
import asyncio
import test_commands
from bot_settings import Bot
import play_song


Bot.bot.run(token=TOKEN)
