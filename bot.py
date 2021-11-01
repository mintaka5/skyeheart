# bot.py
import os
import json

import discord
from discord import Message
from discord.ext import commands
from dotenv import load_dotenv

from tinydb import TinyDB, Query

db = TinyDB('db.json')

load_dotenv()
TOKEN = os.getenv('SKYEHEART_DISCORD_TOKEN')

PREFIX = "->"

client = discord.Client()

"""
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guilds = client.guilds
    for guild in guilds:
        store_members(guild)
"""

@client.event
async def on_connect():
    print(f'Skyeheart has connected')
    app_info = await client.application_info()
    # print(f"Bot owner id: {app_info.owner.id}")

@client.event
async def on_message(message: Message):
    app_info = await client.application_info()
    if message.content.startswith(PREFIX+"help") and message.author.id == app_info.owner.id:
        msg = ""
        msg.join("# HELP\n")
        msg.join("**this is the help**\n")
        print(msg)
        await message.channel.send(msg)


client.run(TOKEN)
