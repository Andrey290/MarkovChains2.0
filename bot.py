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
        print(f"Кто-то прислал сообщение в гильдии {message.guild.name}")
        if message.author == self.user:
            return
        elif "привет" in message.content.lower():
            await message.channel.send("И тебе привет!")
        else:
            smth_to_send = syinon(message.content, message.guild.id, "discord")
            if smth_to_send != "Ничего не придумалось." and random.choice([0, 1, 2, 3, 4, 5]) == 5:
                await message.channel.send(smth_to_send)

client = YLBotClient()
client.run(TOKEN)
