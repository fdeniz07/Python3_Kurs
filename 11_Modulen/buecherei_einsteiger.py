# Bücherei-Verwaltungssystem
# Entwickler: Fatih Deniz
# Erstelldatum: 23.06.2026
# ********************************

# Das ist unsere Datenbank – eine Liste von Wörterbüchern.
# Jedes Wörterbuch (dict) repräsentiert ein Buch mit drei Eigenschaften:
# "Titel", "Autor" und "Jahr".
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019},
    {"Titel": "Datenbankdesign", "Autor": "Hans Müller", "Jahr": 2018},
    {"Titel": "Algorithmen", "Autor": "Sophie Wagner", "Jahr": 2022},
    {"Titel": "Clean Code", "Autor": "Robert C. Martin", "Jahr": 2008},
    {"Titel": "Netzwerke", "Autor": "Peter Klein", "Jahr": 2019},
    {"Titel": "JS", "Autor": "David Flanagan", "Jahr": 2020},
]


# a) Buchsuche
# Diese Funktion sucht nach einem Buch anhand des Titels.
# Der Parameter "autor" ist optional – wenn nichts angegeben wird, ist er None.
def suche_buch(titel, autor=None):
    # Wir erstellen eine leere Liste für die Suchergebnisse
    ergebnisse = []

    # Wir gehen jeden Eintrag in der Datenbank durch
    for buch in buecherei_datenbank:
        # .lower() macht den Vergleich unabhängig von Groß-/Kleinschreibung
        if buch["Titel"].lower() == titel.lower():
            ergebnisse.append(buch)  # Treffer zur Liste hinzufügen

    # Falls ein Autor angegeben wurde, filtern wir die Liste weiter
    if autor:
        gefiltert = []
        for buch in ergebnisse:
            if buch["Autor"].lower() == autor.lower():
                gefiltert.append(buch)
        ergebnisse = gefiltert

    # Die fertige Ergebnisliste wird zurückgegeben
    return ergebnisse


# b) Buch hinzufügen
# Diese Funktion erstellt ein neues Buch als Wörterbuch
# und fügt es der Datenbank hinzu.
def fuege_buch_hinzu(titel, autor, jahr):
    # Wir erstellen ein neues Wörterbuch für das neue Buch
    neues_buch = {"Titel": titel, "Autor": autor, "Jahr": jahr}

    # .append() fügt das neue Buch ans Ende der Liste hinzu
    buecherei_datenbank.append(neues_buch)

    print(f"Buch '{titel}' von {autor} ({jahr}) wurde hinzugefügt.")


# c) Bücher nach Jahr filtern
# Diese Funktion gibt alle Bücher zurück, die in einem bestimmten Jahr erschienen sind.
def buecher_nach_jahr(jahr):
    # Wir erstellen eine leere Ergebnisliste
    ergebnisse = []

    # Wir gehen jeden Eintrag in der Datenbank durch
    for buch in buecherei_datenbank:
        # Wenn das Jahr übereinstimmt, fügen wir das Buch zur Liste hinzu
        if buch["Jahr"] == jahr:
            ergebnisse.append(buch)

    return ergebnisse


# d) Datenbank anzeigen
# Diese Funktion gibt alle Bücher in der Datenbank formatiert aus.
def zeige_datenbank():
    # Prüfen ob die Datenbank leer ist
    if not buecherei_datenbank:
        print("Die Datenbank ist leer.")
        return  # Funktion wird hier beendet

    print("\n--- Bücherei-Datenbank ---")

    # enumerate() gibt uns automatisch eine Nummer (i) und den Wert (buch)
    # start=1 bedeutet: Zählung beginnt bei 1, nicht bei 0
    for i, buch in enumerate(buecherei_datenbank, start=1):
        print(f"{i}. Titel: {buch['Titel']} | Autor: {buch['Autor']} | Jahr: {buch['Jahr']}")

    print("--------------------------\n")


# e) Interaktives Menü
# Diese Funktion zeigt das Hauptmenü an.
def zeige_menue():
    print("\n=== Bücherei-Menü ===")
    print("1. Buch suchen")
    print("2. Buch hinzufügen")
    print("3. Bücher nach Jahr filtern")
    print("4. Datenbank anzeigen")
    print("5. Beenden")
    print("=====================")


# Die Hauptfunktion – hier läuft das gesamte Programm ab.
def main():
    # "while True" bedeutet: Die Schleife läuft endlos,
    # bis wir sie mit "break" manuell beenden.
    while True:
        zeige_menue()
        auswahl = input("Bitte wähle eine Option (1-5): ").strip()  # .strip() entfernt Leerzeichen

        if auswahl == "1":
            titel = input("Titel eingeben: ").strip()
            autor = input("Autor eingeben (optional, Enter zum Überspringen): ").strip()

            # Wenn "autor" leer ist, übergeben wir None (= kein Autor angegeben)
            if autor == "":
                ergebnisse = suche_buch(titel)
            else:
                ergebnisse = suche_buch(titel, autor)

            if ergebnisse:
                print(f"\n{len(ergebnisse)} Buch/Bücher gefunden:")
                for b in ergebnisse:
                    print(f"  - {b['Titel']} von {b['Autor']} ({b['Jahr']})")
            else:
                print("Kein Buch gefunden.")

        elif auswahl == "2":
            titel = input("Titel: ").strip()
            autor = input("Autor: ").strip()

            # try/except fängt Fehler ab – z.B. wenn der Benutzer "abc" statt einer Zahl eingibt
            try:
                jahr = int(input("Erscheinungsjahr: ").strip())  # int() wandelt Text in eine Zahl um
                fuege_buch_hinzu(titel, autor, jahr)
            except ValueError:
                # Dieser Block wird ausgeführt, wenn int() fehlschlägt
                print("Ungültige Jahresangabe. Bitte eine Zahl eingeben.")

        elif auswahl == "3":
            try:
                jahr = int(input("Jahr eingeben: ").strip())
                ergebnisse = buecher_nach_jahr(jahr)

                if ergebnisse:
                    print(f"\nBücher aus dem Jahr {jahr}:")
                    for b in ergebnisse:
                        print(f"  - {b['Titel']} von {b['Autor']}")
                else:
                    print(f"Keine Bücher aus dem Jahr {jahr} gefunden.")
            except ValueError:
                print("Ungültige Jahresangabe. Bitte eine Zahl eingeben.")

        elif auswahl == "4":
            zeige_datenbank()

        elif auswahl == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break  # "break" beendet die while-Schleife

        else:
            # Dieser Block wird ausgeführt, wenn keine gültige Option gewählt wurde
            print("Ungültige Eingabe. Bitte 1 bis 5 wählen.")


# Dieser Block stellt sicher, dass main() nur ausgeführt wird,
# wenn die Datei direkt gestartet wird – nicht wenn sie importiert wird.
if __name__ == "__main__":
    main()
