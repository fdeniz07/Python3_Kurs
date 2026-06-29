import pickle
import os

# Dosya yolu (Program ile aynı dizinde)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATEI_PFAD = os.path.join(BASE_DIR, "planer_daten.pkl")

def daten_laden():
    """Daten aus der .pkl-Datei laden."""
    if not os.path.exists(DATEI_PFAD):
        return []
    # 'rb' = Read Binary (pickle için şart)
    with open(DATEI_PFAD, "rb") as f:
        try:
            return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

def daten_speichern(daten):
    """Daten sicher in die .pkl-Datei speichern."""
    # 'wb' = Write Binary (pickle için şart)
    with open(DATEI_PFAD, "wb") as f:
        pickle.dump(daten, f)

def eintrag_hinzufuegen():
    """Neuen Termin hinzufügen."""
    termin = input("Datum (TT.MM.JJJJ): ")
    inhalt = input("Aktivität: ")
    
    planer = daten_laden()
    planer.append({"datum": termin, "aktivitaet": inhalt})
    
    daten_speichern(planer)
    print("Termin erfolgreich mit Pickle gespeichert!")

def planer_anzeigen():
    """Alle Termine anzeigen."""
    planer = daten_laden()
    print("\n--- Digitaler Planer (Pickle-Modus) ---")
    for eintrag in planer:
        print(f"{eintrag['datum']}: {eintrag['aktivitaet']}")

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