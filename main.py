import discord
import help
import sys
import helpBo5
import helpBo3

TOKEN_TEST = 'OTczODk3OTI4NjQ3Mjc4NTky.GSqXHC.qnhNrpJ0cdyoITGwdhWeIDqm2MmNN01V9Ok4OQ'
TOKEN = 'OTczMTU1NTczNTYwNDEwMTMz.GbBxTb.22P5S-hyWHYQQiZopShucavOB0D1iaRpVpf3sc'

client = discord.Client()

Klase = ["mage", "warrior", "warlock", "demonhunter", "hunter", "paladin", "shaman", "druid", "priest", "rogue"]

Custom = {}

CustomBo5 = {}

Qorder = {}

CustomQorderBo3 = {}

CustomQorderBo5 = {}

QorderCustom = {}

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


'''
Matchupi = []
Decks = main.DataScrapetxt(Matchupi)
'''
Decks, Matchupi = help.DataScrapeCSV()

Decks, Matchupi = help.DeckFixerTXT(Decks, Matchupi, "data.txt", 200)
Decks, Matchupi = help.DeckFixerTXT(Decks, Matchupi, "datahelp.txt", 0)
Decks, Matchupi = help.DeckFixerTXT(Decks, Matchupi, "dataworstcase.txt", 0)

for i in range(len(Matchupi)):
    print(Decks[i], end = " ")
    for j in range(len(Matchupi[i])):
        print(Matchupi[i][j], end = " ")
    print()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.guild:
        channel = 'DM'
    else:
        channel = str(message.channel.name)

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    print(f'{username}: {user_message} ({channel})')

    if user_message.lower() == "!help":
        await message.channel.send(f'{username}, for more info type: !HelpBan or if you have issues beyond that you can contact us at discord Ado#1909 or Hamza#6914')
        return
    if user_message.lower() == "!helpban":
        await message.channel.send(
            f'{username}, current commands you can use are: !Help, !HelpBan, !CustomHelp, !Source, !Bo3Conquest, !StatsBo3Conquest, !Bo5Conquest, !StatsBo5Conquest , !HelpBo3Conquest, !HelpBo5Conquest, !Decks, !qorderbo3, !CustomBo3, !CustomChange')
        return

    if user_message.lower() == "!source":
        await message.channel.send(f'{username}, the source is: https://www.youtube.com/watch?v=r7l0Rq9E8MY')

    if user_message.lower() == "!decks":
        s = ""
        for i in range(len(Decks)):
            s += str(Decks[i])
            s += "\n"
        await message.channel.send(f'{username}, The decks you can use are: \n{s}')
        return

    if user_message.lower() == "!helpbo3conquest":
        await message.channel.send(
            f'{username}, to use !Bo3Conquest you need to write in one line **!Bo3Conquest** as well as all '
            f'6 decks, 3 from you and 3 from your opponent. '
            f'One example of this would be: \n**!Bo3Conquest {Decks[0]} {Decks[1]} {Decks[2]} {Decks[3]} {Decks[4]} {Decks[5]}** \n'
            f'Adding too many or not enough decks will not work as well as using decks not in the database. \n'
            f'The whole input is in one line and you will get the best ban possible statistically. \n'
            f'For a deeper look into the numbers behind the ban write the command **!StatsBo3Conquest** the same way '
            f'you wrote the !Bo3Conquest command!')
        return

    if user_message.lower() == "!helpbo5conquest":
        await message.channel.send(
            f'{username}, to use !Bo5Conquest you need to write in one line **!Bo35onquest** as well as all '
            f'8 decks, 4 from you and 4 from your opponent. '
            f'One example of this would be:\n **!Bo5Conquest {Decks[0]} {Decks[1]} {Decks[2]} {Decks[3]} {Decks[4]} {Decks[5]} {Decks[6]} {Decks[7]}** \n'
            f'Adding too many or not enough decks will not work as well as using decks not in the database. \n'
            f'The whole input is in one line and you will get the best ban possible statistically \n'
            f'For a deeper look into the numbers behind the ban write the command **!StatsBo5Conquest** the same way '
            f'you wrote the !Bo5Conquest command!')
        return

    if user_message.lower() == "!customhelp":
        await message.channel.send(f'{username}, there are three commands for custom bans currently. !CustomBo3Conquest, !CustomChange, !CustomSubmit\n'
                                   f'The first command you have to use is !CustomBo3Conquest. This command is used like the !Bo3Conquest command. If you need '
                                   f'a better explanation for that you can refer to !HelpBo3Conquest. One example of this command is: \n'
                                   f'**!CustomBo3Conquest {Decks[0]} {Decks[1]} {Decks[2]} {Decks[3]} {Decks[4]} reno rogue**\n'
                                   f'If you write this example you will get all the decks that you have to change to be able to see the optimal ban.\n'
                                   f'Of course you can also change pre-existing probabilities as well. To change any probability you have to use the '
                                   f'!CustomChange command. Here is an example of the !CustomChange command: \n'
                                   f'**!CustomChange {Decks[0]} 0.4521 reno rogue**, this way you will edit the probability of {Decks[0]} vs reno rogue\n'
                                   f'You can also use the !CustomChange command with more changes so you do not have to put everything in seperate lines. One'
                                   f'example of this is: \n'
                                   f'**!CustomChange {Decks[1]} 0.9 reno rogue {Decks[2]} 0.9 reno rogue**, this way you can change two probabilities in one line. '
                                   f'You can also do more than two as long as every input is valid.\n'
                                   f'The last command is !CustomSubmit. You can only use this command when every probability is filled or when the bot '
                                   f'tells you that it is ready. After it tells you it is ready you can still change the probabilities of decks. After you submit '
                                   f'by typing **!CustomSubmit** you will get all the probabilities for each ban and a ban suggestion but your data will be deleted '
                                   f'and you will have to do everything from the start.\n'
                                   f'For Bo5 it is a similar system. The only difference is that the commands you use are :\n'
                                   f'**!CustomBo5Conquest**, **!CustomBo5Change** and **!CustomBo5Submit** and there are 8 decks in the !CustomBo5Conquest command instead of 6!')
        return

    if user_message.lower() == "!qorderhelp":
        await message.channel.send(f'To see the queue order for Bo3 matches you can use the !QorderBo3 command. You only need to put !QorderBo3 followed by your 2 '
                                   f'decks and the opponents 2 decks. An example here is: \n'
                                   f'**!QorderBo3 {Decks[0]} {Decks[1]} {Decks[2]} {Decks[3]}**\n'
                                   f'For Bo5 you can use the !QorderBo5 command in a similar way as the !QorderBo3 command, One example of this is: \n'
                                   f'**!QorderBo5 {Decks[0]} {Decks[1]} {Decks[2]} {Decks[3]} {Decks[4]} {Decks[5]}**\n'
                                   f'This command gives you a little bit of info for the first move, it will not give you more info since the amount of data '
                                   f'it could give here is unreadable. Instead **after** your first game you can use the !SecondMoveBo5 command. This command '
                                   f'can be used like this example: \n'
                                   f'**!SecondMoveBo5 {Decks[0]} {Decks[1]} Win**\nThere is a little better explanation for this command after you use the '
                                   f'!QorderBo5 command successfully!')

        return

    if user_message.lower().startswith("!bo3conquest"):
        try:

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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 6:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(
                            f"{username}, your decks aren't valid or in the database, source trust me bro")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 6 decks")
                return
        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
            Dek_za_bananje, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup10, Matchup11, Matchup12 = helpBo3.Banovanje(
                Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3],
                Indeksi_Dekova[4], Indeksi_Dekova[5])
            await message.channel.send(f'{username}, the deck you want to ban is: **{Dek_za_bananje}**.\n')

            return
        except Exception as e:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Oops!", e.__class__, "occurred.")
            pass

    if user_message.lower().startswith("!statsbo3conquest"):
        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 6:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(f"{username}, your decks aren't valid or in the database")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 6 decks")
                return
        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
            Dek_za_bananje, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup10, Matchup11, Matchup12 = helpBo3.Banovanje(
                Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3],
                Indeksi_Dekova[4], Indeksi_Dekova[5])
            await message.channel.send(f'**{username}, the deck you want to ban is: {Dek_za_bananje}**.\n'
                                       f'If you ban {Dekovi[3]}, the chances for a win are: \n'
                                       f'{round(Matchup1 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup2 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup3 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'**Your worst percentage is {round(Matchup4 * 100, 2)}%**\n'
                                       f'If you ban {Dekovi[4]}, the chances for a win are: \n'
                                       f'{round(Matchup5 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup6 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup7 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'**Your worst percentage is {round(Matchup8 * 100, 2)}%**\n'
                                       f'If you ban {Dekovi[5]}, the chances for a win are: \n'
                                       f'{round(Matchup9 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup10 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup11 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'**Your worst percentage is {round(Matchup12 * 100, 2)}%\n**')

            return
        except:
            pass

    if user_message.lower().startswith("!bo5conquest"):
        try:
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
            if len(Dekovi) == 8:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(f"{username}, your decks aren't valid or in the database")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 8 decks")
                return
        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
            Dek_za_bananje, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup10, Matchup11, Matchup12, Matchup13, Matchup14, Matchup15, Matchup16, Matchup17, Matchup18, Matchup19, Matchup20 = helpBo5.BanovanjeBO5(Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3], Indeksi_Dekova[4], Indeksi_Dekova[5], Indeksi_Dekova[6], Indeksi_Dekova[7])
            await message.channel.send(f'{username}, the deck you want to ban is: **{Dek_za_bananje}**.\n')

            return
        except Exception as e:
            print("Oops!", e.__class__ , "occurred.")
            pass

    if user_message.lower().startswith("!statsbo5conquest"):
        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 8:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(
                            f"{username}, your decks aren't valid or in the database, source trust me bro")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 8 decks")
                return
        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))

            '''
            helpBo5.Pomocna()
            '''
            Dek_za_bananje, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup10, Matchup11, Matchup12, Matchup13, Matchup14, Matchup15, Matchup16, Matchup17, Matchup18, Matchup19, Matchup20 = helpBo5.BanovanjeBO5(
                Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3], Indeksi_Dekova[4],
                Indeksi_Dekova[5], Indeksi_Dekova[6], Indeksi_Dekova[7])

            await message.channel.send(f'**{username}, the deck you want to ban is: {Dek_za_bananje}**.\n'
                                       f'If you ban {Dekovi[4]}, the chances for a win are: \n'
                                       f'{round(Matchup1 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup2 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup3 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'{round(Matchup4 * 100, 2)}% if your opponent banned your {Dekovi[3]}\n'
                                       f'**Your worst percentage is {round(Matchup5 * 100, 2)}%**\n'
                                       f'If you ban {Dekovi[5]}, the chances for a win are: \n'
                                       f'{round(Matchup6 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup7 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup8 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'{round(Matchup9 * 100, 2)}% if your opponent banned your {Dekovi[3]}\n'
                                       f'**Your worst percentage is {round(Matchup10 * 100, 2)}%**\n'
                                       f'If you ban {Dekovi[6]}, the chances for a win are: \n'
                                       f'{round(Matchup11 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup12 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup13 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'{round(Matchup14 * 100, 2)}% if your opponent banned your {Dekovi[3]}\n'
                                       f'**Your worst percentage is {round(Matchup15 * 100, 2)}%\n**'
                                       f'If you ban {Dekovi[7]}, the chances for a win are: \n'
                                       f'{round(Matchup16 * 100, 2)}% if your opponent banned your {Dekovi[0]}\n'
                                       f'{round(Matchup17 * 100, 2)}% if your opponent banned your {Dekovi[1]}\n'
                                       f'{round(Matchup18 * 100, 2)}% if your opponent banned your {Dekovi[2]}\n'
                                       f'{round(Matchup19 * 100, 2)}% if your opponent banned your {Dekovi[3]}\n'
                                       f'**Your worst percentage is {round(Matchup20 * 100, 2)}%\n**')
            return
        except:
            pass

    if user_message.lower().startswith("!qorderbo3"):
        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 4:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(f"{username}, your decks aren't valid or in the database, please refer to !QorderHelp if you have any issues!")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 4 decks, please refer to !QorderHelp if you have any issues!")
                return
        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
            DekA, sansaA, DekC, sansaB, DekD, sansaC, DekB, sansaD = helpBo3.QueueOrderBo3(Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3])
            await message.channel.send(f"{username}\nThe chance to win with: {DekA} when your opponent starts with {DekC} is **{round(sansaA*100, 2)}%**\n"
                                       f"The chance to win with: {DekA} when your opponent starts with {DekD} is **{round(sansaB*100, 2)}%**\n"
                                       f"The chance to win with: {DekB} when your opponent starts with {DekC} is **{round(sansaC*100, 2)}%**\n"
                                       f"The chance to win with: {DekB} when your opponent starts with {DekD} is **{round(sansaD*100, 2)}%**\n")
            return
        except:
            pass


    if user_message.lower().startswith("!custombo3conquest"):

        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 6:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                Lista_Dekova = []
                for i in range(len(Dekovi)):
                    if Dekovi[i] in Decks:
                        red = []
                        Indeks_Deka = int(Decks.index(Dekovi[i]))
                        red.append(Dekovi[i])
                        red.append(str(Indeks_Deka))
                        Lista_Dekova.append(red)
                    else:
                        red = []
                        red.append(Dekovi[i])
                        red.append(-1)
                        Lista_Dekova.append(red)
                print(Lista_Dekova)
                for i in range(len(Lista_Dekova)):
                    print(Lista_Dekova[i][1])
                dekovi = []
                red1 = []
                for i in range(3):
                    if Lista_Dekova[i][1] != -1:
                        red = []
                        red.append(Lista_Dekova[i][0])
                        red1.append(Lista_Dekova[i][0])
                        for j in range(3, 6):
                            if Lista_Dekova[j][1] != -1:
                                red.append(str(Matchupi[int(Lista_Dekova[i][1])][int(Lista_Dekova[j][1])]))
                            else:
                                red.append("-1")
                        dekovi.append(red)
                    else:
                        red = []
                        red.append(Lista_Dekova[i][0])
                        red1.append(Lista_Dekova[i][0])
                        for j in range(3, 6):
                            if i != j:
                                if Lista_Dekova[i][0] == Lista_Dekova[j][0]:
                                    red.append("0.5")
                                else:
                                    red.append("-1")
                        dekovi.append(red)
                red = []
                for i in range(3, 6):
                    red.append(Lista_Dekova[i][0])
                dekovi.append(red)
                dekovi.append(red1)
                Custom[username] = dekovi

                izmjene = False
                for i in range(len(dekovi)-2):
                    for j in range(len(dekovi[3])):
                        if dekovi[i][j+1] == "-1":
                            if izmjene == False:
                                s += f'{username}, you need to change the probability between:\n'
                            izmjene = True
                            s += f'**{dekovi[i][0]}** and **{dekovi[3][j]}**\n'

                s += "To change the probabilities you can use the command !CustomChange, please refer to !CustomHelp if you have any issues! "

                if(izmjene == True):
                    await message.channel.send(s)
                else:
                    await message.channel.send(f'{username}, you can use !CustomSubmit to see the most optimal ban for your lineup,'
                                               f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                               f' still use the !CustomChange command or you can use the !CustomHelp command to get a better understanding'
                                               f' of the Custom commands as well as an example of how to do so!')

                print(Custom[username])
                return
            else:
                await message.channel.send(f"{username}, you need exactly 6 decks")
                return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        try:

            return
        except Exception as e:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Oops!", e.__class__, "occurred.")
            pass

    if user_message.lower().startswith("!customchange"):
        if username not in Custom.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo3Conquest successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        try:
            Dekovi = user_message.lower().split(" ")
            Dekovi.pop(0)
            i = 0
            s = ""
            Novi_Dekovi = []
            while i < len(Dekovi):
                if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                    if s != "":
                        print("Ima viska u s: ", s)
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                    Novi_Dekovi.append(Dekovi[i])
                elif Dekovi[i] not in Klase:
                    s += str(Dekovi[i])
                    s += " "
                else:
                    s += str(Dekovi[i])
                    Novi_Dekovi.append(s)
                    s = ""
                i += 1
            Dekovi = Novi_Dekovi
            for i in range(len(Dekovi)):
                if i%3 == 0:
                    if Dekovi[i] not in Custom[username][4]:
                        print(Dekovi[i], "nije broj")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                elif i%3 == 1:
                    if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                        pass
                    else:
                        print(Dekovi[i], "nije u nasim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                else:
                    if Dekovi[i] not in Custom[username][3]:
                        print(Dekovi[i], "nije u protivnickim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        i = 0
        while i<len(Dekovi):
            if i+3>len(Dekovi):
                await message.channel.send(
                    "The input is invalid, please refer to !CustomHelp if you have any issues!")
                print(i+3, ">", len(Dekovi))
                return
            nas_dek = int(Custom[username][4].index(Dekovi[i]))
            i+=1
            izmjena = Dekovi[i]
            i+=1
            njihov_dek = int(Custom[username][3].index(Dekovi[i]))
            i += 1
            print(i)

            Custom[username][nas_dek][njihov_dek+1] = izmjena

        print(Custom[username])
        s = ""
        izmjene = False
        for i in range(len(Custom[username])-2):
            for j in range(len(Custom[username][3])):
                if Custom[username][i][j+1] == "-1":
                    if izmjene == False:
                        s += f'{username}, you need to change the probability between:\n'
                    s += f'**{Custom[username][i][0]}** and **{Custom[username][3][j]}**\n'
                    izmjene = True
        s += "To change the probabilities you can use the command !CustomChange, please refer to !CustomHelp if you have any issues! "

        if izmjene == True:
            await message.channel.send(s)
        else:
            await message.channel.send(f'{username}, you can use !CustomSubmit to see the most optimal ban for your lineup,'
                                       f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                       f' still use the !CustomChange command or you can use the !CustomHelp command to get a better understanding'
                                       f' of the Custom commands as well as an example of how to do so!')

    if user_message.lower() == "!customsubmit":
        if username not in Custom.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo3Conquest successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        Indeks_za_bananje, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup10, Matchup11, Matchup12 = helpBo3.BanovanjeCustom(
            Decks, Matchupi, Custom[username][0][1], Custom[username][0][2], Custom[username][0][3], Custom[username][1][1],
            Custom[username][1][2], Custom[username][1][3], Custom[username][2][1], Custom[username][2][2], Custom[username][2][3])



        await message.channel.send(f'**{username}, the deck you want to ban is: {Custom[username][3][Indeks_za_bananje]}**.\n'
                                   f'If you ban {Custom[username][3][0]}, the chances for a win are: \n'
                                   f'{round(Matchup1 * 100, 2)}% if your opponent banned your {Custom[username][4][0]}\n'
                                   f'{round(Matchup2 * 100, 2)}% if your opponent banned your {Custom[username][4][1]}\n'
                                   f'{round(Matchup3 * 100, 2)}% if your opponent banned your {Custom[username][4][2]}\n'
                                   f'**Your worst percentage is {round(Matchup4 * 100, 2)}%**\n'
                                   f'If you ban {Custom[username][3][1]}, the chances for a win are: \n'
                                   f'{round(Matchup5 * 100, 2)}% if your opponent banned your {Custom[username][4][0]}\n'
                                   f'{round(Matchup6 * 100, 2)}% if your opponent banned your {Custom[username][4][1]}\n'
                                   f'{round(Matchup7 * 100, 2)}% if your opponent banned your {Custom[username][4][2]}\n'
                                   f'**Your worst percentage is {round(Matchup8 * 100, 2)}%**\n'
                                   f'If you ban {Custom[username][3][2]}, the chances for a win are: \n'
                                   f'{round(Matchup9 * 100, 2)}% if your opponent banned your {Custom[username][4][0]}\n'
                                   f'{round(Matchup10 * 100, 2)}% if your opponent banned your {Custom[username][4][1]}\n'
                                   f'{round(Matchup11 * 100, 2)}% if your opponent banned your {Custom[username][4][2]}\n'
                                   f'**Your worst percentage is {round(Matchup12 * 100, 2)}%\n**')


    if user_message.lower().startswith("!custombo5conquest"):

        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 8:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                Lista_Dekova = []
                for i in range(len(Dekovi)):
                    if Dekovi[i] in Decks:
                        red = []
                        Indeks_Deka = int(Decks.index(Dekovi[i]))
                        red.append(Dekovi[i])
                        red.append(str(Indeks_Deka))
                        Lista_Dekova.append(red)
                    else:
                        red = []
                        red.append(Dekovi[i])
                        red.append(-1)
                        Lista_Dekova.append(red)
                print(Lista_Dekova)
                for i in range(len(Lista_Dekova)):
                    print(Lista_Dekova[i][1])
                dekovi = []
                red1 = []
                for i in range(4):
                    if Lista_Dekova[i][1] != -1:
                        red = []
                        red.append(Lista_Dekova[i][0])
                        red1.append(Lista_Dekova[i][0])
                        for j in range(4, 8):
                            if Lista_Dekova[j][1] != -1:
                                red.append(str(Matchupi[int(Lista_Dekova[i][1])][int(Lista_Dekova[j][1])]))
                            else:
                                red.append("-1")
                        dekovi.append(red)
                    else:
                        red = []
                        red.append(Lista_Dekova[i][0])
                        red1.append(Lista_Dekova[i][0])
                        for j in range(4, 8):
                            if i != j:
                                if Lista_Dekova[i][0] == Lista_Dekova[j][0]:
                                    red.append("0.5")
                                else:
                                    red.append("-1")
                        dekovi.append(red)
                red = []
                for i in range(4, 8):
                    red.append(Lista_Dekova[i][0])
                dekovi.append(red)
                dekovi.append(red1)
                CustomBo5[username] = dekovi

                izmjene = False
                for i in range(len(dekovi)-2):
                    for j in range(len(dekovi[4])):
                        if dekovi[i][j+1] == "-1":
                            if izmjene == False:
                                s += f'{username}, you need to change the probability between:\n'
                            izmjene = True
                            s += f'**{dekovi[i][0]}** and **{dekovi[4][j]}**\n'

                s += "To change the probabilities you can use the command !CustomBo5Change, please refer to !CustomHelp if you have any issues! "

                if(izmjene == True):
                    await message.channel.send(s)
                else:
                    await message.channel.send(f'{username}, you can use !CustomBo5Submit to see the most optimal ban for your lineup,'
                                               f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                               f' still use the !CustomBo5Change command or you can use the !CustomHelp command to get a better understanding'
                                               f' of the Custom commands as well as an example of how to do so!')

                print(CustomBo5[username])
                return
            else:
                await message.channel.send(f"{username}, you need exactly 8 decks")
                return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        try:

            return
        except Exception as e:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Oops!", e.__class__, "occurred.")
            pass

    if user_message.lower().startswith("!custombo5change"):
        if username not in CustomBo5.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo5Conquest successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        try:
            Dekovi = user_message.lower().split(" ")
            Dekovi.pop(0)
            i = 0
            s = ""
            Novi_Dekovi = []
            while i < len(Dekovi):
                if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                    if s != "":
                        print("Ima viska u s: ", s)
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                    Novi_Dekovi.append(Dekovi[i])
                elif Dekovi[i] not in Klase:
                    s += str(Dekovi[i])
                    s += " "
                else:
                    s += str(Dekovi[i])
                    Novi_Dekovi.append(s)
                    s = ""
                i += 1
            Dekovi = Novi_Dekovi
            for i in range(len(Dekovi)):
                if i%3 == 0:
                    if Dekovi[i] not in CustomBo5[username][5]:
                        print(Dekovi[i], "nije broj")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                elif i%3 == 1:
                    if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                        pass
                    else:
                        print(Dekovi[i], "nije u nasim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                else:
                    if Dekovi[i] not in CustomBo5[username][4]:
                        print(Dekovi[i], "nije u protivnickim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        i = 0
        while i<len(Dekovi):
            if i+3>len(Dekovi):
                await message.channel.send(
                    "The input is invalid, please refer to !CustomHelp if you have any issues!")
                print(i+3, ">", len(Dekovi))
                return
            nas_dek = int(CustomBo5[username][5].index(Dekovi[i]))
            i+=1
            izmjena = Dekovi[i]
            i+=1
            njihov_dek = int(CustomBo5[username][4].index(Dekovi[i]))
            i += 1
            print(i)

            CustomBo5[username][nas_dek][njihov_dek+1] = izmjena

        print(CustomBo5[username])
        s = ""
        izmjene = False
        for i in range(len(CustomBo5[username])-2):
            for j in range(len(CustomBo5[username][4])):
                if CustomBo5[username][i][j+1] == "-1":
                    if izmjene == False:
                        s += f'{username}, you need to change the probability between:\n'
                    s += f'**{CustomBo5[username][i][0]}** and **{CustomBo5[username][4][j]}**\n'
                    izmjene = True
        s += "To change the probabilities you can use the command !CustomBo5Change, please refer to !CustomHelp if you have any issues! "

        if izmjene == True:
            await message.channel.send(s)
        else:
            await message.channel.send(f'{username}, you can use !CustomBo5Submit to see the most optimal ban for your lineup,'
                                       f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                       f'still use the !CustomBo5Change command or you can use the !CustomHelp command to get a better understanding'
                                       f' of the Custom commands as well as an example of how to do so!')


    if user_message.lower() == "!custombo5submit":
        if username not in CustomBo5.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo5Conquest successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        Indeks_za_bananje, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup10, Matchup11, Matchup12, Matchup13, Matchup14, Matchup15, Matchup16, Matchup17, Matchup18, Matchup19, Matchup20 = helpBo5.BanovanjeBO5Custom(
            CustomBo5[username][0][1], CustomBo5[username][0][2], CustomBo5[username][0][3], CustomBo5[username][0][4], CustomBo5[username][1][1],
            CustomBo5[username][1][2], CustomBo5[username][1][3], CustomBo5[username][1][4], CustomBo5[username][2][1], CustomBo5[username][2][2],
            CustomBo5[username][2][3], CustomBo5[username][2][4], CustomBo5[username][3][1], CustomBo5[username][3][2],
            CustomBo5[username][3][3], CustomBo5[username][3][4])

        await message.channel.send(f'**{username}, the deck you want to ban is: {CustomBo5[username][4][Indeks_za_bananje]}**.\n'
                                   f'If you ban {CustomBo5[username][4][0]}, the chances for a win are: \n'
                                   f'{round(Matchup1 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][0]}\n'
                                   f'{round(Matchup2 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][1]}\n'
                                   f'{round(Matchup3 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][2]}\n'
                                   f'{round(Matchup4 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][3]}\n'
                                   f'**Your worst percentage is {round(Matchup5 * 100, 2)}%**\n'
                                   f'If you ban {CustomBo5[username][4][1]}, the chances for a win are: \n'
                                   f'{round(Matchup6 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][0]}\n'
                                   f'{round(Matchup7 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][1]}\n'
                                   f'{round(Matchup8 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][2]}\n'
                                   f'{round(Matchup9 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][3]}\n'
                                   f'**Your worst percentage is {round(Matchup10 * 100, 2)}%**\n'
                                   f'If you ban {CustomBo5[username][4][2]}, the chances for a win are: \n'
                                   f'{round(Matchup11 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][0]}\n'
                                   f'{round(Matchup12 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][1]}\n'
                                   f'{round(Matchup13 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][2]}\n'
                                   f'{round(Matchup14 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][3]}\n'
                                   f'**Your worst percentage is {round(Matchup15 * 100, 2)}%\n**'
                                   f'If you ban {CustomBo5[username][4][3]}, the chances for a win are: \n'
                                   f'{round(Matchup16 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][0]}\n'
                                   f'{round(Matchup17 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][1]}\n'
                                   f'{round(Matchup18 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][2]}\n'
                                   f'{round(Matchup19 * 100, 2)}% if your opponent banned your {CustomBo5[username][5][3]}\n'
                                   f'**Your worst percentage is {round(Matchup20 * 100, 2)}%\n**')


    if user_message.lower().startswith("!qorderbo5"):
        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 6:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(
                            f"{username}, your decks aren't valid or in the database, please refer to !QorderHelp if you have any issues!")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 6 decks, please refer to !QorderHelp if you have any issues!")
                return
        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
            s= helpBo5.FirstMoveBo5(
                Decks, Matchupi, Indeksi_Dekova[0], Indeksi_Dekova[1], Indeksi_Dekova[2], Indeksi_Dekova[3],
                Indeksi_Dekova[4], Indeksi_Dekova[5])



            await message.channel.send(f'{username}, {s}')
            await message.channel.send(f'To get the full picture **after** your first game type !SecondMoveBo5 and then the deck you used in'
                                       f' your first game, the deck your opponent used in the first game and the result in the form of Win or Loss.'
                                       f' One example of this is if you used {Dekovi[0]}, and your opponent used {Dekovi[3]}, and'
                                       f' you of course won you would write: \n**!SecondMoveBo5 {Dekovi[0]} {Dekovi[3]} Win** \n'
                                       f'If by any chance the opponent cheated and unjustly ofc won against you you would write: \n'
                                       f'**!SecondMoveBo5 {Dekovi[0]} {Dekovi[3]} Loss**')

            Qorder[username] = Indeksi_Dekova
            return
        except Exception as e:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Oops!", e.__class__, "occurred.")
            pass


    if user_message.lower().startswith("!secondmovebo5"):
        Win = 0
        if username not in Qorder.keys():
            await message.channel.send(
                f'You need to use the command !QorderBo5 successfully to be able to use this command, '
                f'please refer to !QorderHelp if you have any issues!')
            return
        try:
            Dekovi = user_message.lower().split(" ")
            Dekovi.pop(0)
            i = 0
            if Dekovi[len(Dekovi)-1] == "win":
                Win = 1
            elif Dekovi[len(Dekovi)-1] == "loss":
                Win = 0
            else:
                return
            Dekovi.pop()

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
                i += 1
            Dekovi = Novi_Dekovi

            for i in range(len(Dekovi)):
                print(Dekovi[i], end=" ")
            if len(Dekovi) == 2:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(
                            f"{username}, your decks aren't valid or in the database, please refer to !QorderHelp if you have any issues!")
                        return
            else:
                await message.channel.send(f"{username}, you need exactly 2 decks, please refer to !QorderHelp if you have any issues!")
                return
        except:
            pass
        try:
            s, s1 = helpBo5.QueueOrderB05(Decks, Matchupi, Qorder[username][0], Qorder[username][1], Qorder[username][2], Qorder[username][3], Qorder[username][4], Qorder[username][5], Dekovi[0], Dekovi[1], Win)
            await message.channel.send(f'{username}, {s}')
            await message.channel.send(f'{s1}')
            del Qorder[username]
            return
        except:
            pass

    if user_message.lower().startswith("!customqorderbo3"):
        PostojanjeDekova = []
        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 4:
                Nasi_Dekovi = []
                Protivnicki_Dekovi = []
                Nasi_Dekovi.append(Dekovi[0])
                Nasi_Dekovi.append(Dekovi[1])
                Protivnicki_Dekovi.append(Dekovi[2])
                Protivnicki_Dekovi.append(Dekovi[3])
                for i in range(len(Dekovi)):
                    red = []
                    red.append(Dekovi[i])
                    if Dekovi[i] not in Decks:
                        red.append("-1")
                    else:
                        red.append(str(Decks.index(Dekovi[i])))
                    PostojanjeDekova.append(red)
                Novi_Dekovi = []
                for i in range(2):
                    red = []
                    red.append(Dekovi[i])
                    for j in range(2):
                        if PostojanjeDekova[i][1] == "-1":
                            if PostojanjeDekova[j + 2][0] == PostojanjeDekova[i][0]:
                                red.append("0.5")
                            else:
                                red.append("-1")
                        else:
                            if PostojanjeDekova[j + 2][1] == "-1":
                                red.append("-1")
                            else:
                                red.append(str(Matchupi[int(PostojanjeDekova[i][1])][int(PostojanjeDekova[j+2][1])]))
                    Novi_Dekovi.append(red)
                Novi_Dekovi.append(Nasi_Dekovi)
                Novi_Dekovi.append(Protivnicki_Dekovi)
                CustomQorderBo3[username] = Novi_Dekovi
                print(Novi_Dekovi)
            else:
                await message.channel.send(f"{username}, you need exactly 4 decks, please refer to !CustomHelp if you have any issues!")
                return

            izmjene = False
            for i in range(len(Novi_Dekovi) - 2):
                for j in range(len(Novi_Dekovi[3])):
                    if Novi_Dekovi[i][j + 1] == "-1":
                        if izmjene == False:
                            s += f'{username}, you need to change the probability between:\n'
                        izmjene = True
                        s += f'**{Novi_Dekovi[i][0]}** and **{Novi_Dekovi[3][j]}**\n'

            s += "To change the probabilities you can use the command !CustomQorderChange, please refer to !CustomHelp if you have any issues! "

            if (izmjene == True):
                await message.channel.send(s)
            else:
                await message.channel.send(
                    f'{username}, you can use !CustomQorderSubmit to see the most optimal ban for your lineup,'
                    f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                    f' still use the !CustomQorderChange command or you can use the !CustomHelp command to get a better understanding'
                    f' of the Custom commands as well as an example of how to do so!')

        except:
            pass

    if user_message.lower().startswith("!customqorderchange"):
        if username not in CustomQorderBo3.keys():
            await message.channel.send(
                f'You need to use the command !CustomQorderBo3 successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        try:
            Dekovi = user_message.lower().split(" ")
            Dekovi.pop(0)
            i = 0
            s = ""
            Novi_Dekovi = []
            while i < len(Dekovi):
                if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                    if s != "":
                        print("Ima viska u s: ", s)
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                    Novi_Dekovi.append(Dekovi[i])
                elif Dekovi[i] not in Klase:
                    s += str(Dekovi[i])
                    s += " "
                else:
                    s += str(Dekovi[i])
                    Novi_Dekovi.append(s)
                    s = ""
                i += 1
            Dekovi = Novi_Dekovi
            for i in range(len(Dekovi)):
                if i%3 == 0:
                    if Dekovi[i] not in CustomQorderBo3[username][2]:
                        print(Dekovi[i], "nije u nasim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                elif i%3 == 1:
                    if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                        pass
                    else:
                        print(Dekovi[i], "nije broj")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                else:
                    if Dekovi[i] not in CustomQorderBo3[username][3]:
                        print(Dekovi[i], "nije u protivnickim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        i = 0
        while i<len(Dekovi):
            if i+3>len(Dekovi):
                await message.channel.send(
                    "The input is invalid, please refer to !CustomHelp if you have any issues!")
                print(i+3, ">", len(Dekovi))
                return
            nas_dek = int(CustomQorderBo3[username][2].index(Dekovi[i]))
            i+=1
            izmjena = Dekovi[i]
            i+=1
            njihov_dek = int(CustomQorderBo3[username][3].index(Dekovi[i]))
            i += 1
            print(i)

            CustomQorderBo3[username][nas_dek][njihov_dek+1] = izmjena

        print(CustomQorderBo3[username])
        s = ""
        izmjene = False
        for i in range(len(CustomQorderBo3[username])-2):
            for j in range(len(CustomQorderBo3[username][3])):
                if CustomQorderBo3[username][i][j+1] == "-1":
                    if izmjene == False:
                        s += f'{username}, you need to change the probability between:\n'
                    s += f'**{CustomQorderBo3[username][i][0]}** and **{CustomQorderBo3[username][3][j]}**\n'
                    izmjene = True
        s += "To change the probabilities you can use the command !CustomQorderChange, please refer to !CustomHelp if you have any issues! "

        if izmjene == True:
            await message.channel.send(s)
        else:
            await message.channel.send(f'{username}, you can use !CustomQorderSubmit to see the most optimal ban for your lineup,'
                                       f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                       f' still use the !CustomQorderChange command or you can use the !CustomHelp command to get a better understanding'
                                       f' of the Custom commands as well as an example of how to do so!')


    if user_message.lower() == "!customqordersubmit":
        if username not in CustomQorderBo3.keys():
            await message.channel.send(
                f'You need to use the command !CustomQorderBo3 successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        DekA, sansaA, DekC, sansaB, DekD, sansaC, DekB, sansaD = helpBo3.CustomQueueOrderBo3(CustomQorderBo3[username])
        await message.channel.send(
            f"{username}\nThe chance to win with: {DekA} when your opponent starts with {DekC} is **{round(sansaA * 100, 2)}%**\n"
            f"The chance to win with: {DekA} when your opponent starts with {DekD} is **{round(sansaB * 100, 2)}%**\n"
            f"The chance to win with: {DekB} when your opponent starts with {DekC} is **{round(sansaC * 100, 2)}%**\n"
            f"The chance to win with: {DekB} when your opponent starts with {DekD} is **{round(sansaD * 100, 2)}%**\n")
        return



    if user_message.lower().startswith("!custombo5qorder"):

        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 6:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                Lista_Dekova = []
                for i in range(len(Dekovi)):
                    if Dekovi[i] in Decks:
                        red = []
                        Indeks_Deka = int(Decks.index(Dekovi[i]))
                        red.append(Dekovi[i])
                        red.append(str(Indeks_Deka))
                        Lista_Dekova.append(red)
                    else:
                        red = []
                        red.append(Dekovi[i])
                        red.append("-1")
                        Lista_Dekova.append(red)
                print(Lista_Dekova)
                for i in range(len(Lista_Dekova)):
                    print(Lista_Dekova[i][1])
                dekovi = []
                red1 = []
                for i in range(3):
                    if Lista_Dekova[i][1] != "-1":
                        red = []
                        red.append(Lista_Dekova[i][0])
                        red1.append(Lista_Dekova[i][0])
                        for j in range(3, 6):
                            if Lista_Dekova[j][1] != "-1":
                                red.append(str(Matchupi[int(Lista_Dekova[i][1])][int(Lista_Dekova[j][1])]))
                            else:
                                red.append("-1")
                        dekovi.append(red)
                    else:
                        red = []
                        red.append(Lista_Dekova[i][0])
                        red1.append(Lista_Dekova[i][0])
                        for j in range(3, 6):
                            if i != j:
                                if Lista_Dekova[i][0] == Lista_Dekova[j][0]:
                                    red.append("0.5")
                                else:
                                    red.append("-1")
                        dekovi.append(red)
                red = []
                for i in range(3, 6):
                    red.append(Lista_Dekova[i][0])
                dekovi.append(red)
                dekovi.append(red1)
                CustomQorderBo5[username] = dekovi

                izmjene = False
                for i in range(len(dekovi)-2):
                    for j in range(len(dekovi[3])):
                        if dekovi[i][j+1] == "-1":
                            if izmjene == False:
                                s += f'{username}, you need to change the probability between:\n'
                            izmjene = True
                            s += f'**{dekovi[i][0]}** and **{dekovi[3][j]}**\n'

                s += "To change the probabilities you can use the command !CustomQorderBo5Change, please refer to !CustomHelp if you have any issues! "

                if(izmjene == True):
                    await message.channel.send(s)
                else:
                    await message.channel.send(f'{username}, you can use !CustomQorderBo5Submit to see the most optimal ban for your lineup,'
                                               f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                               f' still use the !CustomQorderBo5Change command or you can use the !CustomHelp command to get a better understanding'
                                               f' of the Custom commands as well as an example of how to do so!')

                print(CustomQorderBo5[username])
                return
            else:
                await message.channel.send(f"{username}, you need exactly 6 decks")
                return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        try:

            return
        except Exception as e:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Oops!", e.__class__, "occurred.")
            pass

    if user_message.lower().startswith("!customqorderbo5change"):
        if username not in CustomQorderBo5.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo5Qorder successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        try:
            Dekovi = user_message.lower().split(" ")
            Dekovi.pop(0)
            i = 0
            s = ""
            Novi_Dekovi = []
            while i < len(Dekovi):
                if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                    if s != "":
                        print("Ima viska u s: ", s)
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                    Novi_Dekovi.append(Dekovi[i])
                elif Dekovi[i] not in Klase:
                    s += str(Dekovi[i])
                    s += " "
                else:
                    s += str(Dekovi[i])
                    Novi_Dekovi.append(s)
                    s = ""
                i += 1
            Dekovi = Novi_Dekovi
            for i in range(len(Dekovi)):
                if i%3 == 0:
                    if Dekovi[i] not in CustomQorderBo5[username][4]:
                        print(Dekovi[i], "nije broj")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                elif i%3 == 1:
                    if Dekovi[i].startswith("0") or Dekovi[i].startswith("1"):
                        pass
                    else:
                        print(Dekovi[i], "nije u nasim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
                else:
                    if Dekovi[i] not in CustomQorderBo5[username][3]:
                        print(Dekovi[i], "nije u protivnickim dekovima")
                        await message.channel.send("The input is invalid, please refer to !CustomHelp if you have any issues!")
                        return
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
        i = 0
        while i<len(Dekovi):
            if i+3>len(Dekovi):
                await message.channel.send(
                    "The input is invalid, please refer to !CustomHelp if you have any issues!")
                print(i+3, ">", len(Dekovi))
                return
            nas_dek = int(CustomQorderBo5[username][4].index(Dekovi[i]))
            i+=1
            izmjena = Dekovi[i]
            i+=1
            njihov_dek = int(CustomQorderBo5[username][3].index(Dekovi[i]))
            i += 1
            print(i)

            CustomQorderBo5[username][nas_dek][njihov_dek+1] = izmjena

        print(CustomQorderBo5[username])
        s = ""
        izmjene = False
        for i in range(len(CustomQorderBo5[username])-2):
            for j in range(len(CustomQorderBo5[username][3])):
                if CustomQorderBo5[username][i][j+1] == "-1":
                    if izmjene == False:
                        s += f'{username}, you need to change the probability between:\n'
                    s += f'**{CustomQorderBo5[username][i][0]}** and **{CustomQorderBo5[username][3][j]}**\n'
                    izmjene = True
        s += "To change the probabilities you can use the command !CustomQorderBo5Change, please refer to !CustomHelp if you have any issues! "

        if izmjene == True:
            await message.channel.send(s)
        else:
            await message.channel.send(f'{username}, you can use !CustomQorderBo5Submit to see the most optimal ban for your lineup,'
                                       f' once you do this your data will be deleted\nIf you want to further change matchup percentages you can'
                                       f'still use the !CustomQorderBo5Change command or you can use the !CustomHelp command to get a better understanding'
                                       f' of the Custom commands as well as an example of how to do so!')


    if user_message.lower() == "!customqorderbo5submit":
        if username not in CustomQorderBo5.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo5Qorder successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        s = helpBo5.CustomFirstMoveBo5(CustomQorderBo5[username])

        await message.channel.send(f'{username}, {s}')
        await message.channel.send(
            f'To get the full picture **after** your first game type !CustomSecondMoveBo5 and then the deck you used in'
            f' your first game, the deck your opponent used in the first game and the result in the form of Win or Loss.'
            f' One example of this is if you used {CustomQorderBo5[username][4][0]}, and your opponent used {CustomQorderBo5[username][3][0]}, and'
            f' you of course won you would write: \n**!CustomSecondMoveBo5 {CustomQorderBo5[username][4][0]} {CustomQorderBo5[username][3][0]} Win** \n'
            f'If by any chance the opponent cheated and unjustly ofc won against you you would write: \n'
            f'**!CustomSecondMoveBo5 {CustomQorderBo5[username][4][0]} {CustomQorderBo5[username][3][0]} Loss**')

        QorderCustom[username] = CustomQorderBo5[username]
        del CustomQorderBo5[username]
        return


    if user_message.lower().startswith("!customsecondmovebo5"):
        Win = 0
        if username not in QorderCustom.keys():
            await message.channel.send(
                f'You need to use the command !CustomBo5Qorder successfully to be able to use this command, '
                f'please refer to !CustomHelp if you have any issues!')
            return
        try:
            Dekovi = user_message.lower().split(" ")
            Dekovi.pop(0)
            i = 0
            if Dekovi[len(Dekovi)-1] == "win":
                Win = 1
            elif Dekovi[len(Dekovi)-1] == "loss":
                Win = 0
            else:
                return
            Dekovi.pop()

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
                i += 1
            Dekovi = Novi_Dekovi

            for i in range(len(Dekovi)):
                print(Dekovi[i], end=" ")
            if len(Dekovi) == 2:
                for i in range(len(Dekovi)):
                    print(Dekovi[i])
                if Dekovi[0] not in QorderCustom[username][4]:
                    await message.channel.send(
                        f"{username}, your decks aren't valid or in the database, please refer to !CustomHelp if you have any issues!")
                    return
                if Dekovi[1] not in QorderCustom[username][3]:
                    await message.channel.send(
                        f"{username}, your decks aren't valid or in the database, please refer to !CustomHelp if you have any issues!")
                    return
            else:
                await message.channel.send(f"{username}, you need exactly 2 decks, please refer to !CustomHelp if you have any issues!")
                return
        except:
            pass
        try:
            s, s1 = helpBo5.CustomQueueOrderB05(QorderCustom[username],Dekovi[0], Dekovi[1], Win)
            await message.channel.send(f'{username}, {s}')
            await message.channel.send(f'{s1}')
            del QorderCustom[username]
            return
        except:
            pass

    if user_message.lower().startswith("!matchup"):
        try:
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
                i += 1
            Dekovi = Novi_Dekovi
            if len(Dekovi) == 2:
                for i in range(len(Dekovi)):
                    if Dekovi[i] not in Decks:
                        await message.channel.send(
                            f"{username}, your decks aren't valid or in the database")
                        return


            else:
                await message.channel.send(
                    f"{username}, you need exactly 2 decks")
                return


        except:
            pass
        try:
            Indeksi_Dekova = []
            for i in range(len(Dekovi)):
                Indeksi_Dekova.append(int(Decks.index(Dekovi[i])))
            await message.channel.send(f'{username}, the probability of {Dekovi[0]} beating {Dekovi[1]} is {round(Matchupi[Indeksi_Dekova[0]][Indeksi_Dekova[1]] * 100, 2)}%')
        except:
            pass




client.run(TOKEN_TEST)