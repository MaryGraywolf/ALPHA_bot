#Bibliotecas
from this import s
import discord
import datetime
from discord.ext import commands, tasks
import json
import os

with open('configuration.json', 'r') as config:
    data = json.load(config)
    token = data['token']
    prefix = data['prefix']
    owner_id = data['owner_id']

class Greetings(commands.Cog):
    def __init__(self, alpha):
        self.bot = alpha
        self._last_member = None

# Intenções

intents = discord.Intents.default()

# O bot

alpha = commands.Bot(prefix, intents = intents, owner_id = owner_id)

# Carregando ferramenta

if __name__ == '__main__':
    for filename in os.listdir('src'):
        if filename.endswith('.py'):
            alpha.load_extension(f'src.{filename[:-3]}')

@alpha.event
async def on_ready():
    print(f'Auuuuuuu, estou pronto para morder umas bundas! Ass {alpha.user}!')
    print(discord.__version__)
    await alpha.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = f'{alpha.command_prefix}help'))

alpha.run(token)
