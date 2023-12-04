"""
Main entrance to program
"""
from tokens import TOKEN

from bot import Bot

bot = Bot()
bot.bot.run(token=TOKEN)
