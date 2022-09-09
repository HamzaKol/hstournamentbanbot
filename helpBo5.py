import help

def MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9):
    Matchups = []
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup8 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup5 * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup5 * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * Matchup2 * Matchup5 * Matchup8 + (1 - Matchup1) * Matchup2 * Matchup5 * (1 - Matchup8) * Matchup9 + (1 - Matchup1) * Matchup2 * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * (1 - Matchup2) * Matchup3 * Matchup6 * Matchup9)
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup9 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup5 * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup5 * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * Matchup2 * Matchup5 * Matchup9 + (1 - Matchup1) * Matchup2 * Matchup5 * (1 - Matchup9) * Matchup8 + (1 - Matchup1) * Matchup2 * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * (1 - Matchup2) * Matchup3 * Matchup6 * Matchup9)
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup8 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup6 * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup6 * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * Matchup2 * Matchup6 * Matchup8 + (1 - Matchup1) * Matchup2 * Matchup6 * (1 - Matchup8) * Matchup9 + (1 - Matchup1) * Matchup2 * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * (1 - Matchup2) * Matchup3 * Matchup6 * Matchup9)
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup9 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup6 * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup6 * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * Matchup2 * Matchup6 * Matchup9 + (1 - Matchup1) * Matchup2 * Matchup6 * (1 - Matchup9) * Matchup8 + (1 - Matchup1) * Matchup2 * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * (1 - Matchup2) * Matchup3 * Matchup6 * Matchup9)

    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup8 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup5 * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup5 * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * Matchup3 * Matchup5 * Matchup8 + (1 - Matchup1) * Matchup3 * Matchup5 * (1 - Matchup8) * Matchup9 + (1 - Matchup1) * Matchup3 * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * (1 - Matchup3) * Matchup2 * Matchup6 * Matchup9)
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup9 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup5 * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup5 * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * Matchup3 * Matchup5 * Matchup9 + (1 - Matchup1) * Matchup3 * Matchup5 * (1 - Matchup9) * Matchup8 + (1 - Matchup1) * Matchup3 * (1 - Matchup5) * Matchup6 * Matchup9 + (1 - Matchup1) * (1 - Matchup3) * Matchup2 * Matchup6 * Matchup9)
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup8 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup6 * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup6 * (1 - Matchup8) * Matchup9 + Matchup1 * (1 - Matchup4) * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * Matchup3 * Matchup6 * Matchup8 + (1 - Matchup1) * Matchup3 * Matchup6 * (1 - Matchup8) * Matchup9 + (1 - Matchup1) * Matchup3 * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * (1 - Matchup3) * Matchup2 * Matchup6 * Matchup9)
    Matchups.append(Matchup1 * Matchup4 * Matchup7 + Matchup1 * Matchup4 * (1 - Matchup7) * Matchup9 + Matchup1 * Matchup4 * (1 - Matchup7) * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * Matchup6 * Matchup9 + Matchup1 * (1 - Matchup4) * Matchup6 * (1 - Matchup9) * Matchup8 + Matchup1 * (1 - Matchup4) * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * Matchup3 * Matchup6 * Matchup9 + (1 - Matchup1) * Matchup3 * Matchup6 * (1 - Matchup9) * Matchup8 + (1 - Matchup1) * Matchup3 * (1 - Matchup6) * Matchup5 * Matchup9 + (1 - Matchup1) * (1 - Matchup3) * Matchup2 * Matchup6 * Matchup9)

    return(min(Matchups))

def IzmijesajBO5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9):
    Matchups = []
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup9, Matchup7, Matchup8))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup5, Matchup4, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup5, Matchup4, Matchup6, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup5, Matchup4, Matchup6, Matchup9, Matchup7, Matchup8))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup6, Matchup4, Matchup5, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup6, Matchup4, Matchup5, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup1, Matchup2, Matchup3, Matchup6, Matchup4, Matchup5, Matchup9, Matchup7, Matchup8))

    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup4, Matchup5, Matchup6, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup4, Matchup5, Matchup6, Matchup9, Matchup7, Matchup8))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup5, Matchup4, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup5, Matchup4, Matchup6, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup5, Matchup4, Matchup6, Matchup9, Matchup7, Matchup8))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup6, Matchup4, Matchup5, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup6, Matchup4, Matchup5, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup2, Matchup1, Matchup3, Matchup6, Matchup4, Matchup5, Matchup9, Matchup7, Matchup8))

    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup9, Matchup7, Matchup8))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup5, Matchup4, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup5, Matchup4, Matchup6, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup5, Matchup4, Matchup6, Matchup9, Matchup7, Matchup8))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup6, Matchup4, Matchup5, Matchup7, Matchup8, Matchup9))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup6, Matchup4, Matchup5, Matchup8, Matchup7, Matchup9))
    Matchups.append(MatchupiBO5(Matchup3, Matchup1, Matchup2, Matchup6, Matchup4, Matchup5, Matchup9, Matchup7, Matchup8))

    return min(Matchups)



def Kombinacije(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9):
    Matchup = []

    Matchup.append(IzmijesajBO5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9))
    Matchup.append(IzmijesajBO5(Matchup1, Matchup2, Matchup3, Matchup7, Matchup8, Matchup9, Matchup4, Matchup5, Matchup6))

    Matchup.append(IzmijesajBO5(Matchup4, Matchup5, Matchup6, Matchup1, Matchup2, Matchup3, Matchup7, Matchup8, Matchup9))
    Matchup.append(IzmijesajBO5(Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9, Matchup1, Matchup2, Matchup3))

    Matchup.append(IzmijesajBO5(Matchup7, Matchup8, Matchup9, Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6))
    Matchup.append(IzmijesajBO5(Matchup7, Matchup8, Matchup9, Matchup4, Matchup5, Matchup6, Matchup1, Matchup2, Matchup3))

    return max(Matchup)

def BanovanjeBO5(Decks, Matchups, a, b, c, d, e, f, g, h):
    Matchup1 = Matchups[a][e]
    Matchup2 = Matchups[a][f]
    Matchup3 = Matchups[a][g]
    Matchup4 = Matchups[a][h]
    Matchup5 = Matchups[b][e]
    Matchup6 = Matchups[b][f]
    Matchup7 = Matchups[b][g]
    Matchup8 = Matchups[b][h]
    Matchup9 = Matchups[c][e]
    Matchup10 = Matchups[c][f]
    Matchup11 = Matchups[c][g]
    Matchup12 = Matchups[c][h]
    Matchup13 = Matchups[d][e]
    Matchup14 = Matchups[d][f]
    Matchup15 = Matchups[d][g]
    Matchup16 = Matchups[d][h]

    ''' Banujemo Prvi Dek '''

    ''' Banovan nam je prvi dek '''
    MatchupAE = Kombinacije(Matchup6, Matchup7, Matchup8, Matchup10, Matchup11, Matchup12, Matchup14, Matchup15, Matchup16)



    ''' Banovan nam je drugi dek '''

    MatchupBE = Kombinacije(Matchup2, Matchup3, Matchup4, Matchup10, Matchup11, Matchup12, Matchup14, Matchup15,
                            Matchup16)

    ''' Banovan nam je treci dek '''

    MatchupCE = Kombinacije(Matchup2, Matchup3, Matchup4, Matchup6, Matchup7, Matchup8, Matchup14, Matchup15,
                            Matchup16)

    ''' Banovan nam je cetvrti dek '''

    MatchupDE = Kombinacije(Matchup2, Matchup3, Matchup4, Matchup6, Matchup7, Matchup8, Matchup10, Matchup11,
                            Matchup12)

    MatchupE = min(min(MatchupAE, MatchupBE), min(MatchupCE, MatchupDE))

    ''' Banujemo Drugi Dek '''

    ''' Banovan nam je prvi dek '''

    MatchupAF = Kombinacije(Matchup5, Matchup7, Matchup8, Matchup9, Matchup11, Matchup12, Matchup13, Matchup15,
                            Matchup16)

    ''' Banovan nam je drugi dek '''

    MatchupBF = Kombinacije(Matchup1, Matchup3, Matchup4, Matchup9, Matchup11, Matchup12, Matchup13, Matchup15,
                            Matchup16)

    ''' Banovan nam je treci dek '''

    MatchupCF = Kombinacije(Matchup1, Matchup3, Matchup4, Matchup5, Matchup7, Matchup8, Matchup13, Matchup15,
                            Matchup16)

    ''' Banovan nam je cetvrti dek '''

    MatchupDF = Kombinacije(Matchup1, Matchup3, Matchup4, Matchup5, Matchup7, Matchup8, Matchup9, Matchup11,
                            Matchup12)

    MatchupF = min(min(MatchupAF, MatchupBF), min(MatchupCF, MatchupDF))

    ''' Banujemo Treci Dek '''

    ''' Banovan nam je prvi dek '''

    MatchupAG = Kombinacije(Matchup5, Matchup6, Matchup8, Matchup9, Matchup10, Matchup12, Matchup13, Matchup14,
                            Matchup16)

    ''' Banovan nam je drugi dek '''

    MatchupBG = Kombinacije(Matchup1, Matchup2, Matchup4, Matchup9, Matchup10, Matchup12, Matchup13, Matchup14,
                            Matchup16)

    ''' Banovan nam je treci dek '''

    MatchupCG = Kombinacije(Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup8, Matchup13, Matchup14,
                            Matchup16)

    ''' Banovan nam je cetvrti dek '''

    MatchupDG = Kombinacije(Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup8, Matchup9, Matchup10,
                            Matchup12)

    MatchupG = min(min(MatchupAG, MatchupBG), min(MatchupCG, MatchupDG))

    ''' Banujemo cetvrti Dek '''

    ''' Banovan nam je prvi dek '''

    MatchupAH = Kombinacije(Matchup5, Matchup6, Matchup7, Matchup9, Matchup10, Matchup11, Matchup13, Matchup14,
                            Matchup15)

    ''' Banovan nam je drugi dek '''

    MatchupBH = Kombinacije(Matchup1, Matchup2, Matchup3, Matchup9, Matchup10, Matchup11, Matchup13, Matchup14,
                            Matchup15)

    ''' Banovan nam je treci dek '''

    MatchupCH = Kombinacije(Matchup1, Matchup2, Matchup3, Matchup5, Matchup6, Matchup7, Matchup13, Matchup14,
                            Matchup15)

    ''' Banovan nam je cetvrti dek '''

    MatchupDH = Kombinacije(Matchup1, Matchup2, Matchup3, Matchup5, Matchup6, Matchup7, Matchup9, Matchup10,
                            Matchup11)

    MatchupH = min(min(MatchupAH, MatchupBH), min(MatchupCH, MatchupDH))

    if (max(max(MatchupE, MatchupF), max(MatchupG, MatchupH))) == MatchupE:
        i = e
    elif (max(max(MatchupE, MatchupF), max(MatchupG, MatchupH))) == MatchupF:
        i = f
    elif (max(max(MatchupE, MatchupF), max(MatchupG, MatchupH))) == MatchupG:
        i = g
    else:
        i = h

    print(max(max(MatchupE, MatchupF), max(MatchupG, MatchupH)))
    print(MatchupE)
    print(MatchupF)
    print(MatchupG)
    print(MatchupH)

    print("Trebali bi banovati dek: " + str(Decks[int(i)]))

    return str(Decks[int(
        i)]), MatchupAE, MatchupBE, MatchupCE, MatchupDE, MatchupE, MatchupAF, MatchupBF, MatchupCF, MatchupDF, MatchupF, MatchupAG, MatchupBG, MatchupCG, MatchupDG, MatchupG, MatchupAH, MatchupBH, MatchupCH, MatchupDH, MatchupH



def BanovanjeBO5Custom(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):

    Matchup1 = float(a)
    Matchup2 = float(b)
    Matchup3 = float(c)
    Matchup4 = float(d)
    Matchup5 = float(e)
    Matchup6 = float(f)
    Matchup7 = float(g)
    Matchup8 = float(h)
    Matchup9 = float(i)
    Matchup10 = float(j)
    Matchup11 = float(k)
    Matchup12 = float(l)
    Matchup13 = float(m)
    Matchup14 = float(n)
    Matchup15 = float(o)
    Matchup16 = float(p)

    ''' Banujemo Prvi Dek '''

    ''' Banovan nam je prvi dek '''
    MatchupAE = Kombinacije(Matchup6, Matchup7, Matchup8, Matchup10, Matchup11, Matchup12, Matchup14, Matchup15, Matchup16)



    ''' Banovan nam je drugi dek '''

    MatchupBE = Kombinacije(Matchup2, Matchup3, Matchup4, Matchup10, Matchup11, Matchup12, Matchup14, Matchup15,
                            Matchup16)

    ''' Banovan nam je treci dek '''

    MatchupCE = Kombinacije(Matchup2, Matchup3, Matchup4, Matchup6, Matchup7, Matchup8, Matchup14, Matchup15,
                            Matchup16)

    ''' Banovan nam je cetvrti dek '''

    MatchupDE = Kombinacije(Matchup2, Matchup3, Matchup4, Matchup6, Matchup7, Matchup8, Matchup10, Matchup11,
                            Matchup12)

    MatchupE = min(min(MatchupAE, MatchupBE), min(MatchupCE, MatchupDE))

    ''' Banujemo Drugi Dek '''

    ''' Banovan nam je prvi dek '''

    MatchupAF = Kombinacije(Matchup5, Matchup7, Matchup8, Matchup9, Matchup11, Matchup12, Matchup13, Matchup15,
                            Matchup16)

    ''' Banovan nam je drugi dek '''

    MatchupBF = Kombinacije(Matchup1, Matchup3, Matchup4, Matchup9, Matchup11, Matchup12, Matchup13, Matchup15,
                            Matchup16)

    ''' Banovan nam je treci dek '''

    MatchupCF = Kombinacije(Matchup1, Matchup3, Matchup4, Matchup5, Matchup7, Matchup8, Matchup13, Matchup15,
                            Matchup16)

    ''' Banovan nam je cetvrti dek '''

    MatchupDF = Kombinacije(Matchup1, Matchup3, Matchup4, Matchup5, Matchup7, Matchup8, Matchup9, Matchup11,
                            Matchup12)

    MatchupF = min(min(MatchupAF, MatchupBF), min(MatchupCF, MatchupDF))

    ''' Banujemo Treci Dek '''

    ''' Banovan nam je prvi dek '''

    MatchupAG = Kombinacije(Matchup5, Matchup6, Matchup8, Matchup9, Matchup10, Matchup12, Matchup13, Matchup14,
                            Matchup16)

    ''' Banovan nam je drugi dek '''

    MatchupBG = Kombinacije(Matchup1, Matchup2, Matchup4, Matchup9, Matchup10, Matchup12, Matchup13, Matchup14,
                            Matchup16)

    ''' Banovan nam je treci dek '''

    MatchupCG = Kombinacije(Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup8, Matchup13, Matchup14,
                            Matchup16)

    ''' Banovan nam je cetvrti dek '''

    MatchupDG = Kombinacije(Matchup1, Matchup2, Matchup4, Matchup5, Matchup6, Matchup8, Matchup9, Matchup10,
                            Matchup12)

    MatchupG = min(min(MatchupAG, MatchupBG), min(MatchupCG, MatchupDG))

    ''' Banujemo cetvrti Dek '''

    ''' Banovan nam je prvi dek '''

    MatchupAH = Kombinacije(Matchup5, Matchup6, Matchup7, Matchup9, Matchup10, Matchup11, Matchup13, Matchup14,
                            Matchup15)

    ''' Banovan nam je drugi dek '''

    MatchupBH = Kombinacije(Matchup1, Matchup2, Matchup3, Matchup9, Matchup10, Matchup11, Matchup13, Matchup14,
                            Matchup15)

    ''' Banovan nam je treci dek '''

    MatchupCH = Kombinacije(Matchup1, Matchup2, Matchup3, Matchup5, Matchup6, Matchup7, Matchup13, Matchup14,
                            Matchup15)

    ''' Banovan nam je cetvrti dek '''

    MatchupDH = Kombinacije(Matchup1, Matchup2, Matchup3, Matchup5, Matchup6, Matchup7, Matchup9, Matchup10,
                            Matchup11)

    MatchupH = min(min(MatchupAH, MatchupBH), min(MatchupCH, MatchupDH))

    if (max(max(MatchupE, MatchupF), max(MatchupG, MatchupH))) == MatchupE:
        i = 0
    elif (max(max(MatchupE, MatchupF), max(MatchupG, MatchupH))) == MatchupF:
        i = 1
    elif (max(max(MatchupE, MatchupF), max(MatchupG, MatchupH))) == MatchupG:
        i = 2
    else:
        i = 3

    print(max(max(MatchupE, MatchupF), max(MatchupG, MatchupH)))
    print(MatchupE)
    print(MatchupF)
    print(MatchupG)
    print(MatchupH)


    return i, MatchupAE, MatchupBE, MatchupCE, MatchupDE, MatchupE, MatchupAF, MatchupBF, MatchupCF, MatchupDF, MatchupF, MatchupAG, MatchupBG, MatchupCG, MatchupDG, MatchupG, MatchupAH, MatchupBH, MatchupCH, MatchupDH, MatchupH

def WinLossOrderBo5(Matchup1, Matchup2, Matchup3, Matchup4):

    MatchupAC = Matchup1 * Matchup3 + Matchup1 * (1-Matchup3) * Matchup4 + (1-Matchup1) * Matchup2 * Matchup4
    MatchupAD = Matchup2 * Matchup3 + Matchup2 * (1-Matchup3) * Matchup4 + (1-Matchup2) * Matchup1 * Matchup3

    return MatchupAC, MatchupAD


def WinWinOrderBo5(Matchup1, Matchup2, Matchup3):
    return (Matchup1 + (1-Matchup1) * Matchup2 + (1-Matchup1) * (1-Matchup2) * Matchup3)

def WinOrderBo5(Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9):
    MatchupA = WinWinOrderBo5(Matchup7, Matchup8, Matchup9)
    MatchupB = WinWinOrderBo5(Matchup7, Matchup8, Matchup9)
    MatchupC = WinWinOrderBo5(Matchup7, Matchup8, Matchup9)
    MatchupD = WinWinOrderBo5(Matchup4, Matchup5, Matchup6)
    MatchupE = WinWinOrderBo5(Matchup4, Matchup5, Matchup6)
    MatchupF = WinWinOrderBo5(Matchup4, Matchup5, Matchup6)

    MatchupAL1, MatchupAL2 = WinLossOrderBo5(Matchup5, Matchup6, Matchup8, Matchup9)
    MatchupBL1, MatchupBL2 = WinLossOrderBo5(Matchup4, Matchup6, Matchup7, Matchup9)
    MatchupCL1, MatchupCL2 = WinLossOrderBo5(Matchup4, Matchup5, Matchup7, Matchup8)
    MatchupDL1, MatchupDL2 = WinLossOrderBo5(Matchup5, Matchup6, Matchup8, Matchup9)
    MatchupEL1, MatchupEL2 = WinLossOrderBo5(Matchup4, Matchup6, Matchup7, Matchup9)
    MatchupFL1, MatchupFL2 = WinLossOrderBo5(Matchup4, Matchup5, Matchup7, Matchup8)
    Win = []
    Win.append(Matchup4 * MatchupA + (1-Matchup4) * MatchupAL1)
    Win.append(Matchup4 * MatchupA + (1-Matchup4) * MatchupAL2)
    Win.append(Matchup5 * MatchupB + (1-Matchup5) * MatchupBL1)
    Win.append(Matchup5 * MatchupB + (1-Matchup5) * MatchupBL2)
    Win.append(Matchup6 * MatchupC + (1-Matchup6) * MatchupCL1)
    Win.append(Matchup6 * MatchupC + (1-Matchup6) * MatchupCL2)
    Win.append(Matchup7 * MatchupD + (1-Matchup7) * MatchupDL1)
    Win.append(Matchup7 * MatchupD + (1-Matchup7) * MatchupDL2)
    Win.append(Matchup8 * MatchupE + (1-Matchup8) * MatchupEL1)
    Win.append(Matchup8 * MatchupE + (1-Matchup8) * MatchupEL2)
    Win.append(Matchup9 * MatchupF + (1-Matchup9) * MatchupFL1)
    Win.append(Matchup9 * MatchupF + (1-Matchup9) * MatchupFL2)

    return Win

def LossLossOrderBo5(Matchup1, Matchup2, Matchup3):
    return Matchup1 * Matchup2 * Matchup3

def LossWinOrderBo5(Matchup1, Matchup2, Matchup3, Matchup4):

    MatchupAC = Matchup1 * Matchup3 + Matchup1 * (1-Matchup3) * Matchup4 + (1-Matchup1) * Matchup2 * Matchup4
    MatchupAD = Matchup2 * Matchup3 + Matchup2 * (1-Matchup3) * Matchup4 + (1-Matchup2) * Matchup1 * Matchup3

    return MatchupAC, MatchupAD

def LossOrderBo5(Matchup2, Matchup3, Matchup5, Matchup6, Matchup8, Matchup9):
    MatchupA = LossLossOrderBo5(Matchup3, Matchup6, Matchup9)
    MatchupB = LossLossOrderBo5(Matchup2, Matchup5, Matchup8)
    MatchupC = LossLossOrderBo5(Matchup3, Matchup6, Matchup9)
    MatchupD = LossLossOrderBo5(Matchup2, Matchup5, Matchup8)
    MatchupE = LossLossOrderBo5(Matchup3, Matchup6, Matchup9)
    MatchupF = LossLossOrderBo5(Matchup2, Matchup5, Matchup8)

    MatchupAL1, MatchupAL2 = LossWinOrderBo5(Matchup5, Matchup6, Matchup8, Matchup9)
    MatchupBL1, MatchupBL2 = LossWinOrderBo5(Matchup5, Matchup6, Matchup8, Matchup9)
    MatchupCL1, MatchupCL2 = LossWinOrderBo5(Matchup2, Matchup3, Matchup8, Matchup9)
    MatchupDL1, MatchupDL2 = LossWinOrderBo5(Matchup2, Matchup3, Matchup8, Matchup9)
    MatchupEL1, MatchupEL2 = LossWinOrderBo5(Matchup2, Matchup3, Matchup5, Matchup6)
    MatchupFL1, MatchupFL2 = LossWinOrderBo5(Matchup2, Matchup3, Matchup5, Matchup6)
    Loss = []
    Loss.append((1-Matchup2) * MatchupA + Matchup2 * MatchupAL1)
    Loss.append((1-Matchup2) * MatchupA + Matchup2 * MatchupAL2)
    Loss.append((1-Matchup3) * MatchupB + Matchup3 * MatchupBL1)
    Loss.append((1-Matchup3) * MatchupB + Matchup3 * MatchupBL2)
    Loss.append((1-Matchup5) * MatchupC + Matchup5 * MatchupCL1)
    Loss.append((1-Matchup5) * MatchupC + Matchup5 * MatchupCL2)
    Loss.append((1-Matchup6) * MatchupD + Matchup6 * MatchupDL1)
    Loss.append((1-Matchup6) * MatchupD + Matchup6 * MatchupDL2)
    Loss.append((1-Matchup8) * MatchupE + Matchup8 * MatchupEL1)
    Loss.append((1-Matchup8) * MatchupE + Matchup8 * MatchupEL2)
    Loss.append((1-Matchup9) * MatchupF + Matchup9 * MatchupFL1)
    Loss.append((1-Matchup9) * MatchupF + Matchup9 * MatchupFL2)

    return Loss


def FirstMoveBo5(Decks, Matchups, a, b, c, d, e, f):
    Matchup1 = Matchups[a][d]
    Matchup2 = Matchups[a][e]
    Matchup3 = Matchups[a][f]
    Matchup4 = Matchups[b][d]
    Matchup5 = Matchups[b][e]
    Matchup6 = Matchups[b][f]
    Matchup7 = Matchups[c][d]
    Matchup8 = Matchups[c][e]
    Matchup9 = Matchups[c][f]

    MatchupD = max(Matchup1, Matchup4, Matchup7)
    MatchupE = max(Matchup2, Matchup5, Matchup8)
    MatchupF = max(Matchup3, Matchup6, Matchup9)

    s = ""
    s+= f"If your opponent picks {Decks[d]}, then your best first deck is: "
    if Matchup1 == MatchupD:
        s+= f"**{Decks[a]}**\n"
    elif Matchup4 == MatchupD:
        s += f"**{Decks[b]}**\n"
    else:
        s += f"**{Decks[c]}**\n"


    s += f"If your opponent picks {Decks[e]}, then your best first deck is: "
    if Matchup2 == MatchupE:
        s += f"**{Decks[a]}**\n"
    elif Matchup5 == MatchupE:
        s += f"**{Decks[b]}**\n"
    else:
        s += f"**{Decks[c]}**\n"




    s+= f"If your opponent picks {Decks[f]}, then your best first deck is: "
    if Matchup3 == MatchupF:
        s+= f"**{Decks[a]}**\n"
    elif Matchup6 == MatchupF:
        s += f"**{Decks[b]}**\n"
    else:
        s += f"**{Decks[c]}**\n"

    return s

def QueueOrderB05(Decks, Matchups, a, b, c, d, e, f, tvoj, njegov, win):
    Matchup1 = Matchups[a][d]
    Matchup2 = Matchups[a][e]
    Matchup3 = Matchups[a][f]
    Matchup4 = Matchups[b][d]
    Matchup5 = Matchups[b][e]
    Matchup6 = Matchups[b][f]
    Matchup7 = Matchups[c][d]
    Matchup8 = Matchups[c][e]
    Matchup9 = Matchups[c][f]


    if tvoj == Decks[a] and win == 1:
        Win = WinOrderBo5(Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if njegov == Decks[d] and win == 0:
        Win = LossOrderBo5(Matchup2, Matchup3, Matchup5, Matchup6, Matchup8, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if tvoj == Decks[b] and win == 1:
        Win = WinOrderBo5(Matchup1, Matchup2, Matchup3, Matchup7, Matchup8, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if njegov == Decks[e] and win == 0:
        Win = LossOrderBo5(Matchup1, Matchup3, Matchup4, Matchup6, Matchup7, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if tvoj == Decks[c] and win == 1:
        Win = WinOrderBo5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if njegov == Decks[f] and win == 0:
        Win = LossOrderBo5(Matchup1, Matchup2, Matchup4, Matchup5, Matchup7, Matchup8)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1


def CustomFirstMoveBo5(Custom):
    print(Custom[0][1])
    Matchup1 = float(Custom[0][1])
    Matchup2 = float(Custom[0][2])
    Matchup3 = float(Custom[0][3])
    Matchup4 = float(Custom[1][1])
    Matchup5 = float(Custom[1][2])
    Matchup6 = float(Custom[1][3])
    Matchup7 = float(Custom[2][1])
    Matchup8 = float(Custom[2][2])
    Matchup9 = float(Custom[2][3])

    Decks = []
    Decks.append(Custom[4][0])
    Decks.append(Custom[4][1])
    Decks.append(Custom[4][2])
    Decks.append(Custom[3][0])
    Decks.append(Custom[3][1])
    Decks.append(Custom[3][2])

    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5

    MatchupD = max(Matchup1, Matchup4, Matchup7)
    MatchupE = max(Matchup2, Matchup5, Matchup8)
    MatchupF = max(Matchup3, Matchup6, Matchup9)

    s = ""
    s+= f"If your opponent picks {Decks[d]}, then your best first deck is: "
    if Matchup1 == MatchupD:
        s+= f"**{Decks[a]}**\n"
    elif Matchup4 == MatchupD:
        s += f"**{Decks[b]}**\n"
    else:
        s += f"**{Decks[c]}**\n"


    s += f"If your opponent picks {Decks[e]}, then your best first deck is: "
    if Matchup2 == MatchupE:
        s += f"**{Decks[a]}**\n"
    elif Matchup5 == MatchupE:
        s += f"**{Decks[b]}**\n"
    else:
        s += f"**{Decks[c]}**\n"




    s+= f"If your opponent picks {Decks[f]}, then your best first deck is: "
    if Matchup3 == MatchupF:
        s+= f"**{Decks[a]}**\n"
    elif Matchup6 == MatchupF:
        s += f"**{Decks[b]}**\n"
    else:
        s += f"**{Decks[c]}**\n"

    return s

def CustomQueueOrderB05(Custom, tvoj, njegov, win):
    Matchup1 = float(Custom[0][1])
    Matchup2 = float(Custom[0][2])
    Matchup3 = float(Custom[0][3])
    Matchup4 = float(Custom[1][1])
    Matchup5 = float(Custom[1][2])
    Matchup6 = float(Custom[1][3])
    Matchup7 = float(Custom[2][1])
    Matchup8 = float(Custom[2][2])
    Matchup9 = float(Custom[2][3])

    Decks = []
    Decks.append(Custom[4][0])
    Decks.append(Custom[4][1])
    Decks.append(Custom[4][2])
    Decks.append(Custom[3][0])
    Decks.append(Custom[3][1])
    Decks.append(Custom[3][2])

    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5


    if tvoj == Custom[4][0] and win == 1:
        Win = WinOrderBo5(Matchup4, Matchup5, Matchup6, Matchup7, Matchup8, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if njegov == Custom[3][0] and win == 0:
        Win = LossOrderBo5(Matchup2, Matchup3, Matchup5, Matchup6, Matchup8, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if tvoj == Custom[4][1] and win == 1:
        Win = WinOrderBo5(Matchup1, Matchup2, Matchup3, Matchup7, Matchup8, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if njegov == Custom[3][1] and win == 0:
        Win = LossOrderBo5(Matchup1, Matchup3, Matchup4, Matchup6, Matchup7, Matchup9)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if tvoj == Custom[4][2] and win == 1:
        Win = WinOrderBo5(Matchup1, Matchup2, Matchup3, Matchup4, Matchup5, Matchup6)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[f]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[f]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
    if njegov == Custom[3][2] and win == 0:
        Win = LossOrderBo5(Matchup1, Matchup2, Matchup4, Matchup5, Matchup7, Matchup8)
        s = ""
        s1 = ""
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[0] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[1] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[d]}**, is: **{round(Win[2] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[a]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[b]}** into **{Decks[e]}**, is: **{round(Win[3] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[4] * 100, 2)}%**\n"
        s += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[5] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[6] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[b]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[7] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[8] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[d]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[9] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[d]}**, is: **{round(Win[10] * 100, 2)}%**\n"
        s1 += f"Your chance to win after your first move if you pick **{Decks[c]}** into **{Decks[e]}**, and if you lose this matchup and pick **{Decks[a]}** into **{Decks[e]}**, is: **{round(Win[11] * 100, 2)}%**\n"
        return s, s1
'''
Matchups = []

Decks = DataScrapeTXT(Matchups)



Dekovi = []

for i in range(6):
    while True:
        s = input("Upisite " + str(i+1) + ". Dek, prva tri deka su tvoji a ostala tri od protivnika\n" )
        if s in Decks:
            break
        if s == "izadji":
            break
    Dekovi.append(int(Decks.index(s)))

BanovanjeB03(Decks, Matchups, Dekovi[0], Dekovi[1], Dekovi[2], Dekovi[3], Dekovi[4], Dekovi[5])
a = input()
'''