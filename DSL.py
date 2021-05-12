import discord
from discord.ext import commands
import os


#Data
perfix = "gay"
Token = ""
Words = ["key1", "key2", "key3", "key4"]

def get_prefix(client, message):

    prefixes = [perfix]

    return commands.when_mentioned_or(*prefixes)(client, message)

client = commands.Bot(command_prefix=get_prefix)
os.system("clear")
@client.event
async def on_ready():
    print('Bot Is Online And Ready To Roll!')
    print('----------------Info----------------')
    print('Username:', client.user.name)
    print('ID:', client.user.id)

@client.event
async def on_message(message):
  user = client.get_user()
  if message.author !=client.user and isinstance(message.channel, discord.DMChannel):
    await user.send(f"[DM]: {message.author.name}, {message.created_at}, {message.content},{message.attachments}, {message.jump_url}")
  elif not  isinstance(message.channel, discord.DMChannel):
    for w in Words:
      if w in message.content:
        await user.send(f"[SERVER]: {message.guild.name},{message.author.name}, {message.created_at}, {message.content},{message.attachments}, {message.jump_url}")

      

client.run(Token, bot=False)
