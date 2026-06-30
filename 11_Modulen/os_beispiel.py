import os
import time

dateipfad = "beispiel.txt"

# 1. Umgebungsvariablen auslesen (z.B. den Benutzer-Namen)
print(f"Benutzer: {os.environ.get('USERNAME', 'Unbekannt')}")

# 2. Dateigröße prüfen
if os.path.exists(dateipfad):
    groesse = os.path.getsize(dateipfad)
    print(f"Die Datei ist {groesse} Bytes groß.")

    # 3. Zeitstempel der letzten Änderung formatieren
    zeitstempel = os.path.getmtime(dateipfad)
    lesbare_zeit = time.ctime(zeitstempel)
    print(f"Letzte Änderung: {lesbare_zeit}")