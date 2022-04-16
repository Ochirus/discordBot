import discord

from Links.BoobaLinks import BoobaImage

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

client.run(" OTQzMTIzNjkyNDQxOTkzMjE3.YgueYg.INdFXdhwBYDbzXKfBq-YVR9WPnw ")

