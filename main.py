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
    header.pop()
    rows.pop()
    file.close()
    for i in range(len(rows)):
        rows[i].pop()
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = float(rows[i][j])
    return header, rows

def DataScrapeTXT(Matchupi):
    file1 = open("data.txt", "r+")

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
'''Matchup1 = prvi dek sa prvim dekom, Matchup2 = prvi dek sa drugim dekom,
   Matchup3 = drugi dek sa prvim dekom, Matchup4 = drugi dek sa drugim dekom'''

def Matchupi(Matchup1, Matchup2, Matchup3, Matchup4):
    MatchupBECE = Matchup1 * Matchup3 + Matchup1 * (1 - Matchup3) * Matchup4 + (1 - Matchup1) * Matchup2 * Matchup4
    MatchupBECF = Matchup1 * Matchup4 + Matchup1 * (1 - Matchup4) * Matchup3 + (1 - Matchup1) * Matchup2 * Matchup4
    MatchupBFCE = Matchup2 * Matchup3 + Matchup2 * (1 - Matchup3) * Matchup4 + (1 - Matchup2) * Matchup1 * Matchup3
    MatchupBFCF = Matchup2 * Matchup4 + Matchup2 * (1 - Matchup4) * Matchup3 + (1 - Matchup2) * Matchup1 * Matchup3
    Matchup = min(min(MatchupBECE, MatchupBECF), min(MatchupBFCE, MatchupBFCF))
    return Matchup

def Banovanje(Decks, Matchups, a, b, c, d, e, f):
    Matchup1 = Matchups[a][d]
    Matchup2 = Matchups[a][e]
    Matchup3 = Matchups[a][f]
    Matchup4 = Matchups[b][d]
    Matchup5 = Matchups[b][e]
    Matchup6 = Matchups[b][f]
    Matchup7 = Matchups[c][d]
    Matchup8 = Matchups[c][e]
    Matchup9 = Matchups[c][f]





    ''' Banujemo Prvi Dek '''






    ''' Banovan nam je prvi dek '''


    MatchupB = Matchupi(Matchup5, Matchup6, Matchup8, Matchup9)

    MatchupC = Matchupi(Matchup8, Matchup9, Matchup5, Matchup6)

    MatchupBanAD = max(MatchupB, MatchupC)

    ''' Banovan nam je drugi dek '''
    MatchupA = Matchupi(Matchup2, Matchup3, Matchup8, Matchup9)
    MatchupC = Matchupi(Matchup8, Matchup9, Matchup2, Matchup3)

    MatchupBanBD = max(MatchupA, MatchupC)

    ''' Banovan nam je treci dek '''
    MatchupA = Matchupi(Matchup2, Matchup3, Matchup5, Matchup6)
    MatchupB = Matchupi(Matchup5, Matchup6, Matchup2, Matchup3)

    MatchupBanCD = max(MatchupA, MatchupB)


    MatchupBanD = min(MatchupBanAD, min(MatchupBanBD, MatchupBanCD))




    ''' Banujemo Drugi Dek '''






    ''' Banovan nam je prvi dek '''
    MatchupB = Matchupi(Matchup4, Matchup6, Matchup7, Matchup9)
    MatchupC = Matchupi(Matchup7, Matchup9, Matchup4, Matchup6)

    MatchupBanAE = max(MatchupB, MatchupC)

    ''' Banovan nam je drugi dek '''
    MatchupA = Matchupi(Matchup1, Matchup3, Matchup7, Matchup9)
    MatchupC = Matchupi(Matchup7, Matchup9, Matchup1, Matchup3)

    MatchupBanBE = max(MatchupA, MatchupC)

    ''' Banovan nam je treci dek '''
    MatchupA = Matchupi(Matchup1, Matchup3, Matchup4, Matchup6)
    MatchupB = Matchupi(Matchup4, Matchup6, Matchup1, Matchup3)

    MatchupBanCE = max(MatchupA, MatchupB)

    MatchupBanE = min(MatchupBanAE, min(MatchupBanBE, MatchupBanCE))


    ''' Banujemo Treci Dek '''








    ''' Banovan nam je prvi dek '''
    MatchupB = Matchupi(Matchup4, Matchup5, Matchup7, Matchup8)
    MatchupC = Matchupi(Matchup7, Matchup8, Matchup4, Matchup5)

    MatchupBanAF = max(MatchupB, MatchupC)

    ''' Banovan nam je drugi dek '''
    MatchupA = Matchupi(Matchup1, Matchup2, Matchup7, Matchup8)
    MatchupC = Matchupi(Matchup7, Matchup8, Matchup1, Matchup2)

    MatchupBanBF = max(MatchupA, MatchupC)

    ''' Banovan nam je treci dek '''
    MatchupA = Matchupi(Matchup1, Matchup2, Matchup4, Matchup5)
    MatchupB = Matchupi(Matchup4, Matchup5, Matchup1, Matchup2)

    MatchupBanCF = max(MatchupA, MatchupB)

    MatchupBanF = min(MatchupBanAF, min(MatchupBanBF, MatchupBanCF))

    if(max(MatchupBanD, max(MatchupBanE, MatchupBanF))) == MatchupBanD:
        i = d
    elif(max(MatchupBanD, max(MatchupBanE, MatchupBanF))) == MatchupBanE:
        i = e
    else:
        i = f


    print(max(MatchupBanD, max(MatchupBanE, MatchupBanF)))
    print(MatchupBanD)
    print(MatchupBanE)
    print(MatchupBanF)

    print("Trebali bi banovati dek: " + str(Decks[int(i)]))

    return str(Decks[int(i)])


'''
Matchups = []

Decks = DataScrape(Matchups)



Dekovi = []

for i in range(6):
    while True:
        s = input("Upisite " + str(i+1) + ". Dek, prva tri deka su tvoji a ostala tri od protivnika\n" )
        if s in Decks:
            break
        if s == "izadji":
            break
    Dekovi.append(int(Decks.index(s)))

Banovanje(Decks, Matchups, Dekovi[0], Dekovi[1], Dekovi[2], Dekovi[3], Dekovi[4], Dekovi[5])
a = input()
'''