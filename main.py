print("""
*******************************************
Geldautomat Programm

Aufgaben;

1. Guthaben abfragen

2. Geld aufladen

3. Geld abziehen

Um Programm zu beenden bitte 'x' drücken.
*******************************************
""")

guthaben = 1000

while True:
    aufgabe = input("Aufgabe auswählen:")

    if ( aufgabe == "x"):
        print("Auf Wiedersehen")
        break
    elif (aufgabe == "1"):
        print("Ihr Guthaben beträgt {}".format(guthaben))
    elif (aufgabe == "2"):
        menge = int(input("Menge eingeben:"))
        guthaben += menge
    elif (aufgabe =="3"):
        menge = int(input("Menge eingeben:"))

        if (guthaben - menge < 0):
            print("Diese Menge nicht abziehbar")
            continue
        guthaben -= menge
