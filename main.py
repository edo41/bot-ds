import discord

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

canali = ["bot", "test-bot"]

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")

    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$peppe brescia'):
        await message.channel.send("buonsalve")
    elif message.content.startswith('glamour'):
        await message.channel.send("GLAMOUR PEPPE BRESCIAAAAA")
    elif message.content.startswith('marco b porterai minecraft?'):
        await message.channel.send("Maincraf eh.. no")
    else:
        if f"{message.channel}" in canali:
            await message.channel.send(message.content)

client.run("token privato non si ruba non si fa hihihi")
