import discord
import asyncio
import random
import json
from constants import *
from functions import syinon, chain_probability_calc, generation


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        print("Кто-то поздоровался.")
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        print("Кто-то прислал сообщение.")
        if message.author == self.user:
            return
        elif "привет" in message.content.lower():
            await message.channel.send("И тебе привет")
        elif len(message.content) > 15:
            await message.channel.send(syinon(message.content, message.guild.id))

client = YLBotClient()
client.run(TOKEN)
