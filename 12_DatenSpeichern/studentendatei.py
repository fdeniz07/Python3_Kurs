def speichere_daten(studenten_liste):
    """Speichert eine Liste von Studenten-Tupeln in einer Textdatei."""
    try:
        with open(r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\studentendaten.txt", "w", encoding="utf-8") as f:
            for name, matrikel, studiengang in studenten_liste:
                f.write(f"Name: {name}, Matrikelnummer: {matrikel}, Studiengang: {studiengang}\n")
        print("Daten wurden erfolgreich in 'studentendaten.txt' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")

def lade_daten():
    """Liest Studentendaten aus der Datei und gibt sie als Liste von Dictionaries zurück."""
    studenten_dicts = []
    try:
        with open(r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\studentendaten.txt", "r", encoding="utf-8") as f:
            for zeile in f:
                # Entfernt Zeilenumbruch und splittet den String
                zeile = zeile.strip()
                teile = zeile.split(", ")
                
                # Extrahiert die Werte hinter den Labels
                name = teile[0].replace("Name: ", "")
                matrikel = teile[1].replace("Matrikelnummer: ", "")
                studiengang = teile[2].replace("Studiengang: ", "")
                
                studenten_dicts.append({
                    "Name": name, 
                    "Matrikelnummer": matrikel, 
                    "Studiengang": studiengang
                })
        return studenten_dicts
    except FileNotFoundError:
        print("Fehler: Die Datei 'studentendaten.txt' wurde nicht gefunden.")
        return []
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return []

# --- Beispielaufruf ---
studierende = [
    ("Max Mustermann", "12345", "Informatik"),
    ("Erika Musterfrau", "67890", "Mathematik")
]

# Daten speichern
speichere_daten(studierende)

# Daten laden und anzeigen
geladene_studenten = lade_daten()
print("\nGeladene Daten:")
for s in geladene_studenten:
    print(s)