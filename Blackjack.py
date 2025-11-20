from Spel_onderdelen import Kaart, Deler, Speler # bijv. Spel_onderdelen.Kaart() kan ook
import random # kaarten geschud, verschillende volgorde, shuffle

spelregels = "Het doel is om de deler te verslaan door dichter bij 21 punten te komen dan de deler. Als je meer dan 21 punten hebt, verlies je ongeacht wat de deler heeft."
print(spelregels)

winsten = 0
verliezen = 0

while True:
    deler = Deler()
    speler = Speler()
    stapel = []

    harten = "\u2764\uFE0F" # ❤️
    ruiten = "\u2666\uFE0F" # ♦️
    klaveren = "\u2663\uFE0F" # ♣️
    schoppen = "\u2660\uFE0F" # ♠️

    # 52 kaarten
    stapel.append(Kaart(10, harten, " harten heer"))
    stapel.append(Kaart(10, harten, " harten dame"))
    stapel.append(Kaart(10, harten, " harten aas"))
    stapel.append(Kaart(10, harten, " harten boer"))
    stapel.append(Kaart(10, harten, " harten"))  # 10
    stapel.append(Kaart(9, harten, " harten")) # 9
    stapel.append(Kaart(8, harten, " harten")) # 8
    stapel.append(Kaart(7, harten, " harten")) # 7
    stapel.append(Kaart(6, harten, " harten")) # 6
    stapel.append(Kaart(5, harten, " harten")) # 5
    stapel.append(Kaart(4, harten, " harten")) # 4
    stapel.append(Kaart(3, harten, " harten")) # 3
    stapel.append(Kaart(2, harten, " harten")) # 2
    # stapel.append(Kaart(1,"❤️ ", "harten 1"))

    stapel.append(Kaart(10, ruiten, " ruiten heer"))
    stapel.append(Kaart(10, ruiten, " ruiten dame"))
    stapel.append(Kaart(10, ruiten, " ruiten aas"))
    stapel.append(Kaart(10, ruiten, " ruiten boer"))
    stapel.append(Kaart(10, ruiten, " ruiten"))  # 10
    stapel.append(Kaart(9, ruiten, " ruiten")) # 9
    stapel.append(Kaart(8, ruiten, " ruiten")) # 8
    stapel.append(Kaart(7, ruiten, " ruiten")) # 7
    stapel.append(Kaart(6, ruiten, " ruiten")) # 6
    stapel.append(Kaart(5, ruiten, " ruiten")) # 5
    stapel.append(Kaart(4, ruiten, " ruiten")) # 4
    stapel.append(Kaart(3, ruiten, " ruiten")) # 3
    stapel.append(Kaart(2, ruiten, " ruiten")) # 2
    # stapel.append(Kaart(1,"♦️ ", "ruiten 1"))

    stapel.append(Kaart(10, klaveren, " klaveren heer"))
    stapel.append(Kaart(10, klaveren, " klaveren dame"))
    stapel.append(Kaart(10, klaveren, " klaveren aas"))
    stapel.append(Kaart(10, klaveren, " klaveren boer"))
    stapel.append(Kaart(10, klaveren, " klaveren")) # 10
    stapel.append(Kaart(9, klaveren, " klaveren")) # 9
    stapel.append(Kaart(8, klaveren, " klaveren")) # 8
    stapel.append(Kaart(7, klaveren, " klaveren")) # 7
    stapel.append(Kaart(6, klaveren, " klaveren")) # 6
    stapel.append(Kaart(5, klaveren, " klaveren")) # 5
    stapel.append(Kaart(4, klaveren, " klaveren")) # 4
    stapel.append(Kaart(3, klaveren, " klaveren")) # 3
    stapel.append(Kaart(2, klaveren, " klaveren")) # 2
    # stapel.append(Kaart(1,"♣️ ", "klaveren 1"))

    stapel.append(Kaart(10, schoppen, " schoppen heer"))
    stapel.append(Kaart(10, schoppen, " schoppen dame"))
    stapel.append(Kaart(10, schoppen, " schoppen aas"))
    stapel.append(Kaart(10, schoppen, " schoppen boer"))
    stapel.append(Kaart(10, schoppen, " schoppen")) # 10
    stapel.append(Kaart(9, schoppen, " schoppen")) # 9
    stapel.append(Kaart(8, schoppen, " schoppen")) # 8
    stapel.append(Kaart(7, schoppen, " schoppen")) # 7
    stapel.append(Kaart(6, schoppen, " schoppen")) # 6
    stapel.append(Kaart(5, schoppen, " schoppen")) # 5
    stapel.append(Kaart(4, schoppen, " schoppen")) # 4
    stapel.append(Kaart(3, schoppen, " schoppen")) # 3
    stapel.append(Kaart(2, schoppen, " schoppen")) # 2
    # stapel.append(Kaart(1,"♠️ ", "schoppen 1"))

    # for kaart in stapel:
    #     print(kaart)

    random.shuffle(stapel)

    deler.hand.append(stapel.pop())
    deler.hand.append(stapel.pop())

    speler.hand.append(stapel.pop())
    speler.hand.append(stapel.pop())

    print("\nDeler heeft: ")
    for kaart in deler.hand:
        print(kaart)
    print("\nScore van de deler: ", deler.bereken_score())

    print("\nSpeler heeft: ")
    for kaart in speler.hand:
        print(kaart)
    print("\nScore van de speler: ", speler.bereken_score())

    while True:
        hit_or_call = input("\nHit (krijg een kaart) of Call (stop het spel): ").lower().strip()
        if hit_or_call == "hit":
            print("\nHit: krijg een kaart")
            speler.hand.append(stapel.pop())
            speler.hand[-1]
            print("\nSpeler heeft: ")
            for kaart in speler.hand:
                print(kaart)
            print("\nScore van de speler: ", speler.bereken_score())
            if speler.bereken_score() >= 21: # >= (21 of meer)
                break
            continue

        elif hit_or_call == "call":
            print("\nCall: spel gestopt")
            print("\nScore deler: ", deler.bereken_score())
            print("Score speler: ", speler.bereken_score())
            break
        elif hit_or_call not in ["hit", "call"]:
            print(f"{hit_or_call} is ongeldig, typ hit of call")
            continue

    if deler.bereken_score() > 21: # > (meer dan 21)
        print("\nSpeler wint, deler heeft 21+")
        winsten += 1
    elif speler.bereken_score() > 21:
        print("\nDeler wint, speler heeft 21+")
        verliezen += 1
    elif speler.bereken_score() == 21:
        print("\nSpeler wint, speler heeft 21")
    elif speler.bereken_score() > deler.bereken_score():
        print("\nSpeler wint, speler heeft meer dan deler")
        winsten += 1
    elif deler.bereken_score() > speler.bereken_score():
        print("\nDeler wint, deler heeft meer dan speler")
        verliezen += 1
    elif speler.bereken_score() == deler.bereken_score():
        print("\nGelijkspel, speler wint")
        winsten += 1
    else:
        print("\nNiemand wint")

    print(f"\nTotaal gewonnen: {winsten}")
    print(f"Totaal verloren: {verliezen}")

    opnieuw = input("\nTyp ja om opnieuw te spelen: ").lower().strip()
    if opnieuw != "ja":
        print("Spel beëindigd")
        break