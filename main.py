import discord
from discord.ext import commands
from tokens import TOKEN
import asyncio


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', self_bot=True, intents=intents)

@bot.command()
async def hello_world(ctx):
    await ctx.send('Hello World!\n')


bot.run(token=TOKEN)