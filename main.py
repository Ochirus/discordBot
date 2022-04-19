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

    if message.content.startswith('>get henti'):
        hentaiLib = HentaiLib(None, None)

        if message.content.startswith('>get henti -title'):
            hentaiLib.SetAuthor(message.content)
            hentaiLib.SetTitle(message.content)
            await message.channel.send(hentaiLib.GetLink())

        if message.content.startswith('>get henti -author'):
            hentaiLib.SetAuthor(message.content)
            await message.channel.send(hentaiLib.GetRandomAuthorLink())

        if message.content.startswith('>get henti -r'):
            hentaiLib.GetRandomLink()
            for iterator in range(hentaiLib.GetTag_contents_size()):
                await message.channel.send(hentaiLib.GetLinkImage(iterator))

client.run("  ")

