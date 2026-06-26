# Bücherei-Verwaltungssystem
# Entwickler: Fatih Deniz
# Erstelldatum: 23.06.2026
# ********************************
# Bücherei-Datenbank
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


# Suche von Büchern nach Titel und optional nach Autor
def suche_buch(titel, autor=None):
    ergebnis = []

    for buch in buecherei_datenbank:
        if autor is None:
            if buch["Titel"].lower() == titel.lower():
                ergebnis.append(buch)
        else:
            if (buch["Titel"].lower() == titel.lower() and
                    buch["Autor"].lower() == autor.lower()):
                ergebnis.append(buch)

    return ergebnis


# Hinzufügen von Büchern zur Datenbank
def fuege_buch_hinzu(titel, autor, jahr):
    neues_buch = {
        "Titel": titel,
        "Autor": autor,
        "Jahr": jahr
    }

    buecherei_datenbank.append(neues_buch)
    print("Buch erfolgreich hinzugefügt.")


# Suche von Büchern nach Erscheinungsjahr
def buecher_nach_jahr(jahr):
    return list(
        filter(
            lambda buch: buch["Jahr"] == jahr,
            buecherei_datenbank
        )
    )


# Anzeige der gesamten Datenbank
def zeige_datenbank():
    print("\n===== BÜCHEREI-DATENBANK =====")

    for buch in buecherei_datenbank:
        print(
            f"Titel: {buch['Titel']}, "
            f"Autor: {buch['Autor']}, "
            f"Jahr: {buch['Jahr']}"
        )


# Hauptmenü
while True:

    print("\n===== MENÜ =====")
    print("1 - Buch suchen")
    print("2 - Buch hinzufügen")
    print("3 - Bücher nach Jahr suchen")
    print("4 - Datenbank anzeigen")
    print("5 - Beenden")

    auswahl = input("Bitte wählen: ")

    if auswahl == "1":
        titel = input("Titel: ")
        autor = input("Autor (optional): ")

        if autor == "":
            ergebnis = suche_buch(titel)
        else:
            ergebnis = suche_buch(titel, autor)

        if len(ergebnis) == 0:
            print("Keine Bücher gefunden.")
        else:
            for buch in ergebnis:
                print(buch)

    elif auswahl == "2":
        titel = input("Titel: ")
        autor = input("Autor: ")
        jahr = int(input("Jahr: "))

        fuege_buch_hinzu(titel, autor, jahr)

    elif auswahl == "3":
        jahr = int(input("Jahr: "))

        ergebnis = buecher_nach_jahr(jahr)

        if len(ergebnis) == 0:
            print("Keine Bücher gefunden.")
        else:
            for buch in ergebnis:
                print(buch)

    elif auswahl == "4":
        zeige_datenbank()

    elif auswahl == "5":
        print("Programm wird beendet.")
        break

    else:
        print("Ungültige Eingabe.")