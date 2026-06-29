# daten_speichern.py
import os

# a) Funktion zum Speichern der Daten mit Fehlerbehandlung (c)
def speichere_daten(personen_liste, dateiname="personen.txt"):
    try:
        # Öffnen der Datei mit der 'with'-Anweisung im Schreibmodus 'w'
        with open(dateiname, "w", encoding="utf-8") as datei:
            for name, alter in personen_liste:
                # Formatierte Speicherung: Name: Alter
                datei.write(f"{name}: {alter}\n")
        print(f"[Erfolg] Daten wurden erfolgreich in '{dateiname}' gespeichert.")
    except IOError as e:
        # c) Abfangen von Schreib-/Lesefehlern
        print(f"[Fehler] Beim Schreiben in die Datei '{dateiname}' ist ein Fehler aufgetreten: {e}")
    except Exception as e:
        print(f"[Unbekannter Fehler] Fehler beim Speichern: {e}")

# b) Funktion zum Laden der Daten mit Fehlerbehandlung (c)
def lade_daten(dateiname="personen.txt"):
    geladene_daten = []
    
    # c) Fehlerbehandlung: Überprüfen, ob die Datei überhaupt existiert
    if not os.path.exists(dateiname):
        print(f"[Fehler] Die Datei '{dateiname}' existiert nicht.")
        return geladene_daten

    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile_nummer, zeile in enumerate(datei, 1):
                zeile = zeile.strip()
                if not zeile:
                    continue  # Leere Zeilen überspringen
                
                # Zeile am Trennzeichen ': ' splitten
                if ": " in zeile:
                    name, alter_str = zeile.split(": ", 1)
                    try:
                        alter = int(alter_str)
                        # Als Dictionary in der Liste speichern
                        geladene_daten.append({"Name": name, "Alter": alter})
                    except ValueError:
                        print(f"[Warnung] Ungültiges Alter in Zeile {zeile_nummer}: '{zeile}'")
                else:
                    print(f"[Warnung] Ungültiges Zeilenformat in Zeile {zeile_nummer}: '{zeile}'")
        return geladene_daten
    except IOError as e:
        print(f"[Fehler] Beim Lesen der Datei '{dateiname}' ist ein Fehler aufgetreten: {e}")
        return []
    except Exception as e:
        print(f"[Unbekannter Fehler] Fehler beim Laden: {e}")
        return []

# Hauptprogramm zur Demonstration der Funktionalitäten
if __name__ == "__main__":
    # Testdaten definieren (Liste von Tupeln)
    test_personen = [
        ("Anna Müller", 28),
        ("Maximilian Schmidt", 34),
        ("Elena Petrova", 22),
        ("Jonas Wagner", 45)
    ]
    
    print("--- Schritt 1: Daten speichern (a) ---")
    speichere_daten(test_personen)
    
    print("\n--- Schritt 2: Daten laden (b) ---")
    personen_dictionaries = lade_daten()
    
    print("\n--- Schritt 3: Kontrollstruktur & Ausgabe (d) ---")
    # d) Kontrollstruktur zur Überprüfung, ob die Liste leer ist oder nicht
    if personen_dictionaries:
        print(f"Es wurden {len(personen_dictionaries)} Personen geladen:\n")
        
        # Formatierte Tabellen-Ausgabe mithilfe einer Schleife
        print(f"{'Name':<25} | {'Alter':<5}")
        print("-" * 35)
        for person in personen_dictionaries:
            print(f"{person['Name']:<25} | {person['Alter']:<5}")
    else:
        print("[Hinweis] Die Liste ist leer oder es konnten keine Daten geladen werden.")