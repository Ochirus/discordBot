import discord

from Links.BoobaLinks import BoobaImage
from Links.HentaiLibLinks import HentaiLib

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        await message.channel.send('Hello!')

    if message.author.id == 355760210591219712:
        await message.channel.send('fuck you')

    if message.content.startswith('>get booba'):
        boobaImage = BoobaImage('link', 'name', [])
        if message.content.startswith('>get booba -r'):
            await message.channel.send(boobaImage.GetBoobaLinksRandom())
        if message.content.startswith('>get booba -l'):
            await message.channel.send(boobaImage.GetBoobaLinkLast())

    if message.content.startswith('>get henti -r'):
        hentaiLib = HentaiLib(None, None)
        await message.channel.send(hentaiLib.GetRandomLink())

client.run(" OTQzMTIzNjkyNDQxOTkzMjE3.YgueYg.k2O9uOSEHN8DNa6eBRYieCTK76Q ")

