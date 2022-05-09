import discord
import main
import citanje

TOKEN = 'OTczMTU1NTczNTYwNDEwMTMz.GbBxTb.22P5S-hyWHYQQiZopShucavOB0D1iaRpVpf3sc'

client = discord.Client()

Klase = ["mage", "warrior", "warlock", "demonhunter", "hunter", "paladin", "shaman", "druid", "priest", "rogue"]

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


'''
Matchupi = []
Decks = main.DataScrapetxt(Matchupi)
'''
Decks, Matchupi = main.DataScrapeCSV()


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return


    if user_message.lower().startswith("!bo3conquest"):
        Dekovi = user_message.lower().split(" ")
        Dekovi.pop(0)
        i = 0
        s = ""
        Novi_Dekovi = []
        while i < len(Dekovi):
            if Dekovi[i] not in Klase:
                s += str(Dekovi[i])
                s += " "
            else:
                s += str(Dekovi[i])
                Novi_Dekovi.append(s)
                s = ""
            i+=1
        Dekovi = Novi_Dekovi
        for i in range(len(Dekovi)):
            print(Dekovi[i])
        for i in range(len(Dekovi)):
            if Dekovi[i] not in Decks:
                await message.channel.send(f"{username}, your decks aren't valid or in the database")
                return

        Indeksi_Dekova = []
        for i in range(len(Dekovi)):
            Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
        Dek_za_bananje = main.Banovanje(Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3], Indeksi_Dekova[4], Indeksi_Dekova[5])
        await message.channel.send(f'{username}, the deck you want to ban is: {Dek_za_bananje}')
        return
'''
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username}')
            return
'''

client.run(TOKEN)