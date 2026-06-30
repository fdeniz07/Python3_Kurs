import json
import os

# Dateinamen
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_DATEI = os.path.join(BASE_DIR, "namen.txt")
JSON_DATEI = os.path.join(BASE_DIR, "namen.json")

def lese_namen_aus_datei():
    """Liest Namen zeilenweise aus einer Textdatei."""
    namen = []
    try:
        with open(TXT_DATEI, "r", encoding="utf-8") as f:
            for zeile in f:
                namen.append(zeile.strip())
        print(f"{len(namen)} Namen erfolgreich aus '{TXT_DATEI}' gelesen.")
        return namen
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{TXT_DATEI}' wurde nicht gefunden.")
        return []
    except IOError as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return []

def speichere_namen_als_json(namen_liste):
    """Speichert eine Liste von Namen im JSON-Format."""
    try:
        with open(JSON_DATEI, "w", encoding="utf-8") as f:
            json.dump(namen_liste, f, indent=4)
        print(f"Daten erfolgreich als JSON in '{JSON_DATEI}' gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der JSON-Datei: {e}")

def main():
    """Benutzeroberfläche zur Steuerung."""
    while True:
        print("\n--- Namens-Verwaltung ---")
        print("1: Namen aus Textdatei laden")
        print("2: Namen als JSON speichern")
        print("3: Beenden")
        
        auswahl = input("Wahl: ")
        
        if auswahl == "1":
            liste = lese_namen_aus_datei()
            print("Geladene Namen:", liste)
        elif auswahl == "2":
            liste = lese_namen_aus_datei()
            if liste:
                speichere_namen_als_json(liste)
            else:
                print("Keine Namen zum Speichern vorhanden.")
        elif auswahl == "3":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")

if __name__ == "__main__":
    main()