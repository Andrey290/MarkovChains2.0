import discord
import json
import asyncio
from main import syinon

TOKEN = "ODMxNjIxOTcxNDg1MzkyOTY2.YHX6UA.ivLQwYNE4xChss3Tu00TzIpCRQ4"

class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        print(123)
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        print(2345)
        if message.author == self.user:
            return
        elif "привет" in message.content.lower():
            await message.channel.send("И тебе привет")
        elif len(message.content) > 15:
            await message.channel.send(syinon(message.content))
        else:
            await message.channel.send("Спасибо за сообщение")


client = YLBotClient()
client.run(TOKEN)