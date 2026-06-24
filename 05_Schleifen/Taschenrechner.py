
# Taschenrechner
# Entwickler: Fatih Deniz
# Erstelldatum: 11.06.2026
# ********************************

# Die äußere while-Schleife ermöglicht
# die wiederholte Nutzung des Taschenrechners.
while True:

    print("\nBitte wählen Sie eine Operation:")
    print("A - Addition")
    print("S - Subtraktion")
    print("M - Multiplikation")
    print("D - Division")

    # Diese Schleife stellt sicher,dass nur gültige Operatoren eingegeben werden.
    while True:

        operator = input("Ihre Auswahl: ").upper()

        if operator in ("A", "S", "M", "D"):
            break
        else:
            print("Fehler: Bitte nur A, S, M oder D eingeben.")

    # Der Benutzer gibt zwei Zahlen ein.
    try:
        zahl1 = float(input("Bitte geben Sie die erste Zahl ein: "))
        zahl2 = float(input("Bitte geben Sie die zweite Zahl ein: "))

    except ValueError:
        print("Fehler: Bitte nur Zahlen eingeben.")
        continue

    # Diese if-elif-else-Struktur überprüft, welche Operation ausgewählt wurde.
    if operator == "A":

        ergebnis = zahl1 + zahl2
        print("Ergebnis:", ergebnis)

    elif operator == "S":

        ergebnis = zahl1 - zahl2
        print("Ergebnis:", ergebnis)

    elif operator == "M":

        ergebnis = zahl1 * zahl2
        print("Ergebnis:", ergebnis)

    elif operator == "D":

        # Diese Kontrollstruktur verhindert
        # eine Division durch Null.
        if zahl2 == 0:
            print("Fehler: Division durch Null ist nicht erlaubt.")
        else:
            ergebnis = zahl1 / zahl2
            print("Ergebnis:", ergebnis)

    # Diese Schleife fragt den Benutzer, ob eine weitere Berechnung durchgeführt werden soll.
    while True:

        weiter = input(
            "\nMöchten Sie eine weitere Berechnung durchführen? (J/N): "
        ).upper()

        if weiter == "J":
            break

        elif weiter == "N":
            print("Programm wird beendet.")
            exit()

        else:
            print("Bitte nur J oder N eingeben.")

