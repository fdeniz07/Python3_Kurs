import json
import os

# Setze den Dateipfad relativ zum aktuellen Skript-Standort
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATEI_PFAD = os.path.join(BASE_DIR, "planer_daten.json")

def daten_laden():
    """Lädt die Daten aus der JSON-Datei. Bei Fehlern wird eine leere Liste zurückgegeben."""
    if not os.path.exists(DATEI_PFAD):
        return []
    
    # Prüfe, ob die Datei leer ist
    if os.path.getsize(DATEI_PFAD) == 0:
        return []

    with open(DATEI_PFAD, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Fehler: Die Datei ist beschädigt. Starte mit einer leeren Liste.")
            return []

def daten_speichern(daten):
    """Speichert die Daten sicher in die JSON-Datei."""
    with open(DATEI_PFAD, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4)

def eintrag_hinzufuegen():
    """Fügt einen neuen Termin hinzu."""
    datum = input("Datum (TT.MM.JJJJ): ")
    inhalt = input("Aktivität: ")
    
    planer = daten_laden()
    planer.append({"datum": datum, "aktivitaet": inhalt})
    
    daten_speichern(planer)
    print("Termin erfolgreich gespeichert!")

def planer_anzeigen():
    """Zeigt alle gespeicherten Termine an, mit Fehlerabfangung."""
    planer = daten_laden()
    
    if not planer:
        print("\nDer Planer ist leer.")
        return

    print("\n--- Digitaler Planer ---")
    for eintrag in planer:
        # Hier prüfen wir, ob 'eintrag' ein Dictionary oder ein String ist
        if isinstance(eintrag, dict):
            print(f"{eintrag.get('datum', 'Unbekannt')}: {eintrag.get('aktivitaet', 'Keine Aktivität')}")
        else:
            # Wenn es ein String ist, drucken wir ihn einfach direkt aus
            print(f"Eintrag: {eintrag}")

# Hauptmenü
while True:
    print("\n1: Termin hinzufügen | 2: Planer anzeigen | 3: Beenden")
    auswahl = input("Wahl: ")
    if auswahl == "1":
        eintrag_hinzufuegen()
    elif auswahl == "2":
        planer_anzeigen()
    elif auswahl == "3":
        print("Auf Wiedersehen!")
        break