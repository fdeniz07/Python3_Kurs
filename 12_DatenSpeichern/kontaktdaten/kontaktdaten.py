import json
import os

DATEI_PFAD = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\kontaktdaten\\kontaktdaten.json"

def lade_kontakte():
    """Liest die Kontakte aus der JSON-Datei. Gibt eine Liste zurück."""
    if not os.path.exists(DATEI_PFAD):
        return []
    
    try:
        with open(DATEI_PFAD, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Fehler beim Laden der Kontakte: {e}")
        return []

def speichere_kontakt(name, email, telefon):
    """Fügt einen neuen Kontakt hinzu, ohne bestehende Daten zu löschen."""
    kontakte = lade_kontakte()
    
    neuer_kontakt = {
        "Name": name,
        "E-Mail": email,
        "Telefon": telefon
    }
    
    kontakte.append(neuer_kontakt)
    
    try:
        with open(DATEI_PFAD, "w", encoding="utf-8") as f:
            json.dump(kontakte, f, indent=4)
        print("Kontakt erfolgreich gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern: {e}")

def cli_interface():
    """Einfache Benutzeroberfläche zur Kontaktverwaltung."""
    while True:
        print("\n--- Kundenkontakt-Verwaltung ---")
        print("1: Neuen Kontakt hinzufügen")
        print("2: Alle Kontakte anzeigen")
        print("3: Beenden")
        
        wahl = input("Auswahl: ")
        
        if wahl == "1":
            name = input("Name: ")
            email = input("E-Mail: ")
            telefon = input("Telefonnummer: ")
            speichere_kontakt(name, email, telefon)
        elif wahl == "2":
            kontakte = lade_kontakte()
            if not kontakte:
                print("Keine Kontakte gefunden.")
            else:
                for k in kontakte:
                    print(f"\nName: {k['Name']}\nE-Mail: {k['E-Mail']}\nTelefon: {k['Telefon']}")
        elif wahl == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    cli_interface()