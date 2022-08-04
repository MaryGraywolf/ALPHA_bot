#Bibliotecas
import discord
import datetime
from discord.ext import commands, tasks
import os

class MyClient(discord.Client):

    async def on_ready(self):
        print('Auuuuuuu, estou pronto para morder umas bundas! Ass {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == "!regras":
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}')

        # filtro de palavrões
        palavreado = ['tnc', 'caralho', 'porra', 'buceta']

        for i in palavreado:
            if message.content == i:
                await message.channel.send(f'Por favor, @{message.author.name}, não ofenda os demais usuários!!')
                await message.delete()


        """ if message.content == '!report':
            message = message.get_channel('ID')
            await message.channel.send(f'{message.author.name} abriu uma denuúncia contra o(a)') """


# bot.get_channel(id do canal) para mandar a mensagem para um determinado canal
#.report @user <reason>

client = MyClient()
# LEMBRAR DE TIRAR A CHAVE DE ACESSO DO BOT ANTES DE COMMITAR
client.run('token')
##TESTE ANA
