import json
import os

# Pfad-Konfiguration für die Datei
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATEI_NAME = os.path.join(BASE_DIR, "freunde.txt")

# a) Liste mit den Namen von fünf Freunden erstellen
freunde = ["Anna", "Bernd", "Clara", "David", "Elena"]

def freunde_speichern(liste):
    """Speichert die Liste im JSON-Format."""
    try:
        # f) with-Anweisung garantiert das korrekte Schließen
        with open(DATEI_NAME, "w", encoding="utf-8") as file:
            json.dump(liste, file, indent=4) # indent=4 für bessere Lesbarkeit (leerbare Formatierung)
        print("Erfolg: Die Liste wurde in 'freunde.txt' gespeichert.")
    except IOError as e:
        # e) Fehlerbehandlung beim Schreiben
        print(f"Fehler beim Schreiben der Datei: {e}")

def freunde_lesen():
    """Liest die Liste aus der Datei."""
    try:
        with open(DATEI_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        # e) Fehlerbehandlung beim Lesen
        print(f"Fehler beim Lesen der Datei: {e}")
        return []

# --- Programmablauf ---

# b) Speichern der ursprünglichen Liste
freunde_speichern(freunde)

# c) Liste aus der Datei lesen und einer neuen Variable zuweisen
erste_freunde_liste = freunde_lesen()
print(f"Erste Liste aus Datei: {erste_freunde_liste}")

# d) Einen Namen hinzufügen, ohne das ursprüngliche 'freunde'-Objekt zu ändern
erste_freunde_liste.append("Felix")
freunde_speichern(erste_freunde_liste)

# Endergebnis lesen
letzte_freunde_liste = freunde_lesen()
print(f"Aktualisierte Liste: {letzte_freunde_liste}")