# ---------------------------------------------
# Stimmungsabfrage mit Kontrollstrukturen
# Autor: Fatih Deniz
# ---------------------------------------------

# Die äußere while-Schleife sorgt dafür,
# dass das Programm wiederholt wird,
# bis der Benutzer es beenden möchte.
while True:

    print("\nBitte wählen Sie Ihre aktuelle Stimmung:")
    print("1 - glücklich")
    print("2 - traurig")
    print("3 - müde")

    stimmung = int(input("Ihre Auswahl: "))

    # Diese if-elif-else-Struktur überprüft,
    # welche Stimmung der Benutzer ausgewählt hat.
    if stimmung == 1:
        print("Es ist toll zu hören, dass du glücklich bist!")

    elif stimmung == 2:
        print("Es tut mir leid zu hören, dass du traurig bist.")
        print("Ich hoffe, es geht dir bald besser!")

    elif stimmung == 3:
        print("Vielleicht solltest du dich etwas ausruhen.")
        print("Ruhe ist wichtig.")

    else:
        print("Interessant! Ich weiß nicht viel über diese Stimmung.")

    # Diese innere while-Schleife stellt sicher,
    # dass der Benutzer nur J oder N eingeben kann.
    while True:

        beenden = input("\nProgramm beenden? (J/N): ")

        # Diese if-Struktur prüft,
        # ob der Benutzer das Programm beenden möchte.
        if beenden.upper() == "J":
            print("Programm wird beendet.")
            exit()

        elif beenden.upper() == "N":
            print("Das Programm wird neu gestartet.")
            break

        else:
            print("Ungültige Eingabe! Bitte nur J oder N eingeben.")

