tupel = ('A', 'z', 'T', 1, 9)

while True:

    versuche = 3
    gewonnen = False

    while versuche > 0:
        tipp = input("Geben Sie einen Tipp ein: ")

        if tipp in [str(x) for x in tupel]:
            print("Richtig! Ihr Tipp befindet sich im Tupel.")
            gewonnen = True
            break

        versuche -= 1
        print(f"Leider falsch. Verbleibende Versuche: {versuche}")

    if gewonnen:
        auswahl = input(
            "\nDrücken Sie 'N' für ein neues Spiel oder eine beliebige Taste zum Beenden: "
        )

        if auswahl.lower() == "n":
            continue
        else:
            print("Programm wird beendet.")
            break

    print("\nIhre Versuche sind aufgebraucht.")

    auswahl = input(
        "Drücken Sie 'N' für einen Neustart oder eine beliebige Taste zum Beenden: "
    )

    if auswahl.lower() != "n":
        print("Programm wird beendet.")
        break
