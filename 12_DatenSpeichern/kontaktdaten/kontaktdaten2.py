import json
import os

DATEI_PFAD = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\kontaktdaten\\kontaktdaten.json"

def speichere_kontakt(name, email, telefon):

    kontakt = {'Name': name, 'E-Mail': email, 'Telefonnummer': telefon}
    try:
        with open(DATEI_PFAD, 'r+') as file:
            daten = json.load(file)
            daten.append(kontakt)
            file.seek(0)
            json.dump(daten, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(DATEI_PFAD, 'w') as file:
            json.dump([kontakt], file, indent=4)
        print("Neue Datei wurde erstellt, da keine vorhanden war.")
def lade_kontakte():
    try:
        with open(DATEI_PFAD, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Fehler beim Laden der Kontakte. Datei existiert nicht oder ist beschädigt.")
        return []
def benutzeroberflaeche():
    while True:
        aktion = input("Möchten Sie einen neuen Kontakt speichern (s) oder vorhandene Kontakte anzeigen (a)? (s/a/beenden): ")
        if aktion.lower() == 'beenden':
            break
        elif aktion.lower() == 's':
            name = input("Name: ")
            email = input("E-Mail: ")
            telefon = input("Telefonnummer: ")
            speichere_kontakt(name, email, telefon)
            print("Kontakt gespeichert.")
        elif aktion.lower() == 'a':
            kontakte = lade_kontakte()
            if kontakte:
                for kontakt in kontakte:
                    print(f"Name: {kontakt['Name']}, E-Mail: {kontakt['E-Mail']}, Telefonnummer: {kontakt['Telefonnummer']}")
            else:
                print("Keine Kontakte gefunden.")
        else:
            print("Ungültige Eingabe.")
if __name__ == "__main__":
    benutzeroberflaeche()