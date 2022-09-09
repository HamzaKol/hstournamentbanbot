def DataScrapeCSV():
    import csv
    file = open("matchupTable.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)


    for i in range(len(rows)):
        rows[i].pop(0)


    for i in range(len(header)):
        header[i] = str(header[i].lower())



    header.pop(0)
    file.close()

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = float(rows[i][j])
    return header, rows

def DataScrapeTXT(Matchupi):
    file1 = open("matchupTable.txt", "r+")

    Decks = file1.readline().split("\t")

    for i in range(len(Decks)):
        red = file1.readline().split("\t")
        Matchupi.append(red)

    for i in range(len(Decks)):
        Decks[i] = Decks[i].lower()

    for i in range(len(Matchupi)):
        if ("\n" in Matchupi[i]):
            Matchupi[i].remove("\n")
        if ("" in Matchupi[i]):
            Matchupi[i].remove("")

    if ("" in Matchupi):
        Matchupi.remove("")
    if ([] in Matchupi):
        Matchupi.remove([])

    for i in range(len(Matchupi)):
        for j in range(len(Matchupi[0])):
            Matchupi[i][j] = float(Matchupi[i][j])

    return Decks

def DeckFixerTXT(Decks, Matchupi, name, games):
    file = open(name, "r+")

    while True:
        try:
            ime_deka = file.readline()
        except Exception as e:
            print("Ooops", e.__class__, " lmao lol")
            break
        if not ime_deka:
            break
        if ime_deka == "Not enough games\n":
            file.readline()
            file.readline()
            continue
        if ime_deka.startswith("TwitchTwitch"):
            continue
        ime_deka = ime_deka.replace("\n", "")
        ime_deka = ime_deka.lower()
        if ime_deka in Decks:
            Indeks_Deka = int(Decks.index(ime_deka))
        else:
            Decks.append(ime_deka)
            Indeks_Deka = int(Decks.index(ime_deka))
            red = []
            for i in range(len(Matchupi)):
                Matchupi[i].append(-1)
            for i in range(len(Decks) - 1):
                red.append(-1)
            red.append(0.5)
            Matchupi.append(red)
        pomocni = file.readline().split("\t", 1)
        if pomocni[0] == "Mirror matchup\n":
            Matchupi[Indeks_Deka][Indeks_Deka] = 0.5
            continue
        else:
            ime_protivnickog_deka = pomocni[1]
            ime_protivnickog_deka = ime_protivnickog_deka.replace("\n", "")
            ime_protivnickog_deka = ime_protivnickog_deka.lower()
            if ime_protivnickog_deka in Decks:
                Indeks_Deka_Protivnika = int(Decks.index(ime_protivnickog_deka))
                file.readline()
                pomocni = file.readline().split("\t")
                broj_gameova = pomocni[1]
                broj_gameova = broj_gameova.replace("\n", "")
                broj_gameova = broj_gameova.replace(",", "")
                sansa = file.readline()
                if sansa.startswith("Twitch"):
                    sansa = file.readline()
                sansa = sansa.replace("\n", "")
                sansa = sansa.replace("%", "")
                if(int(broj_gameova) > games):
                    if Matchupi[Indeks_Deka][Indeks_Deka_Protivnika] == -1:
                        Matchupi[Indeks_Deka][Indeks_Deka_Protivnika] = round(float(sansa)/100, 4)
                        Matchupi[Indeks_Deka_Protivnika][Indeks_Deka] = round(float(1-(float(sansa))/100), 4)
            else:
                file.readline()
                broj_gameova = file.readline().split("\t")
                sansa = file.readline()
                if sansa.startswith("Twitch"):
                    sansa = file.readline()
    return Decks, Matchupi