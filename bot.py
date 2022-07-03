from code import InteractiveInterpreter
import cmds
import discord

guild = discord.Guild
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Up and running!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('_'):
        cmd = message.content.split()[0].replace("_", "")
        parameters = []
        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:]

        if cmd == 'purge':
            await cmds.purge(message)

client.run('')
