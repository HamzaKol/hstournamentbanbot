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

    return str(Decks[int(i)]), MatchupBanAD, MatchupBanBD, MatchupBanCD, MatchupBanD, MatchupBanAE, MatchupBanBE, MatchupBanCE, MatchupBanE, MatchupBanAF, MatchupBanBF, MatchupBanCF, MatchupBanF

def QueueOrderBo3(Decks, Matchups, a, b, c, d):
    Matchup1 = Matchups[a][c]
    Matchup2 = Matchups[a][d]
    Matchup3 = Matchups[b][c]
    Matchup4 = Matchups[b][d]

    MatchupAC = Matchup1 * Matchup3 + Matchup1 * (1-Matchup3) * Matchup4 + (1-Matchup1) * Matchup2 * Matchup4
    MatchupAD = Matchup2 * Matchup3 + Matchup2 * (1-Matchup3) * Matchup4 + (1-Matchup2) * Matchup1 * Matchup3
    MatchupBC = Matchup3 * Matchup1 + Matchup3 * (1-Matchup1) * Matchup2 + (1-Matchup3) * Matchup4 * Matchup2
    MatchupBD = Matchup4 * Matchup1 + Matchup4 * (1-Matchup1) * Matchup2 + (1-Matchup4) * Matchup3 * Matchup1

    print(MatchupAC, end=" ")
    print(MatchupAD, end=" ")
    print(MatchupBC, end=" ")
    print(MatchupBD)

    return str(Decks[int(a)]), MatchupAC, str(Decks[int(c)]), MatchupAD, str(Decks[int(d)]), MatchupBC, str(Decks[int(b)]), MatchupBD


def BanovanjeCustom(Decks, Matchups, a, b, c, d, e, f, g, h, i):
    Matchup1 = float(a)
    Matchup2 = float(b)
    Matchup3 = float(c)
    Matchup4 = float(d)
    Matchup5 = float(e)
    Matchup6 = float(f)
    Matchup7 = float(g)
    Matchup8 = float(h)
    Matchup9 = float(i)





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
        i = 0
    elif(max(MatchupBanD, max(MatchupBanE, MatchupBanF))) == MatchupBanE:
        i = 1
    else:
        i = 2


    print(max(MatchupBanD, max(MatchupBanE, MatchupBanF)))
    print(MatchupBanD)
    print(MatchupBanE)
    print(MatchupBanF)


    return i, MatchupBanAD, MatchupBanBD, MatchupBanCD, MatchupBanD, MatchupBanAE, MatchupBanBE, MatchupBanCE, MatchupBanE, MatchupBanAF, MatchupBanBF, MatchupBanCF, MatchupBanF


def CustomQueueOrderBo3(Custom):
    Matchup1 = float(Custom[0][1])
    Matchup2 = float(Custom[0][2])
    Matchup3 = float(Custom[1][1])
    Matchup4 = float(Custom[1][2])

    MatchupAC = Matchup1 * Matchup3 + Matchup1 * (1-Matchup3) * Matchup4 + (1-Matchup1) * Matchup2 * Matchup4
    MatchupAD = Matchup2 * Matchup3 + Matchup2 * (1-Matchup3) * Matchup4 + (1-Matchup2) * Matchup1 * Matchup3
    MatchupBC = Matchup3 * Matchup1 + Matchup3 * (1-Matchup1) * Matchup2 + (1-Matchup3) * Matchup4 * Matchup2
    MatchupBD = Matchup4 * Matchup1 + Matchup4 * (1-Matchup1) * Matchup2 + (1-Matchup4) * Matchup3 * Matchup1

    print(MatchupAC, end=" ")
    print(MatchupAD, end=" ")
    print(MatchupBC, end=" ")
    print(MatchupBD)

    return Custom[0][0], MatchupAC, Custom[3][0], MatchupAD, Custom[3][1], MatchupBC, Custom[1][0], MatchupBD



'''
Decks, Matchups = DataScrapeCSV()

print(Decks)
print(Matchups)



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
