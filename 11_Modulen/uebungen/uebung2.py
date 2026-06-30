'''
Aufgabe: Systemumgebung
Entwickle ein Python-Skript, das folgende Funktionen implementiert:

a) Erstelle eine Funktion erstelle_datei, die eine neue Textdatei mit einem vorgegebenen Namen 
und Inhalt in einem spezifischen Verzeichnis erstellt. Verwende dazu die with-Anweisung und stelle sicher, 
dass Fehler, wie z.B. fehlende Schreibberechtigungen, mit try und except abgefangen werden.

b) Implementiere eine Funktion listdir_filter, die alle Dateien eines Verzeichnisses auflistet, 
die eine bestimmte Dateiendung haben (z.B. .txt). Nutze dazu das Modul os und eine List Comprehension.

c) Schreibe eine Funktion umbenennen_dateien, die alle Dateien eines Verzeichnisses, 
die eine bestimmte Endung haben, umbenennt, indem sie ein Präfix hinzufügt. Verwende dazu das Modul os.

d) Entwickle eine Funktion json_speichern, die eine Liste von Dictionaries in eine Datei im JSON-Format speichert. 
Verwende dazu das Modul json.

e) Implementiere eine Funktion json_laden, die eine JSON-Datei liest und den Inhalt als Python-Objekt zurückgibt.

f) Erstelle eine Funktion regex_suche, die in allen .txt-Dateien eines Verzeichnisses nach 
einem regulären Ausdruck sucht und die Namen der Dateien zurückgibt, in denen die Suche erfolgreich war.

Für jede dieser Funktionen sollst du ein kurzes Beispiel für deren Aufruf und Verwendung schreiben. 
'''

import os
import json
import re


# a) Neue Textdatei erstellen
def erstelle_datei(verzeichnis, dateiname, inhalt):
    try:
        if not os.path.exists(verzeichnis):
            os.mkdir(verzeichnis)

        dateipfad = os.path.join(verzeichnis, dateiname)

        with open(dateipfad, "w", encoding="utf-8") as datei:
            datei.write(inhalt)

        print(f"Datei '{dateiname}' wurde erfolgreich erstellt.")

    except PermissionError:
        print("Fehler: Keine Schreibberechtigung.")
    except Exception as fehler:
        print(f"Fehler: {fehler}")


# b) Dateien mit bestimmter Endung auflisten
def listdir_filter(verzeichnis, endung):
    return [datei for datei in os.listdir(verzeichnis)
            if datei.endswith(endung)]


# c) Dateien umbenennen
def umbenennen_dateien(verzeichnis, endung, praefix):
    for datei in os.listdir(verzeichnis):
        if datei.endswith(endung) and not datei.startswith(praefix):
            alter_pfad = os.path.join(verzeichnis, datei)
            neuer_name = praefix + datei
            neuer_pfad = os.path.join(verzeichnis, neuer_name)

            if not os.path.exists(neuer_pfad):
                os.rename(alter_pfad, neuer_pfad)

    print("Dateien wurden umbenannt.")


# d) JSON speichern
def json_speichern(dateiname, daten):
    with open(dateiname, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)

    print("JSON-Datei wurde gespeichert.")


# e) JSON laden
def json_laden(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:
        return json.load(datei)


# f) Regulären Ausdruck in Textdateien suchen
def regex_suche(verzeichnis, regex):
    gefundene_dateien = []

    for datei in os.listdir(verzeichnis):
        if datei.endswith(".txt"):
            pfad = os.path.join(verzeichnis, datei)

            with open(pfad, "r", encoding="utf-8") as f:
                inhalt = f.read()

                if re.search(regex, inhalt):
                    gefundene_dateien.append(datei)

    return gefundene_dateien


# --------------------------------------------------
# Beispiele
# --------------------------------------------------

# a)
erstelle_datei(
    "MeineDaten2",
    "beispiel.txt",
    "Hallo! Dies ist eine Beispieldatei."
)

# b)
txt_dateien = listdir_filter("MeineDaten2", ".txt")
print("TXT-Dateien:", txt_dateien)

# c)
umbenennen_dateien("MeineDaten2", ".txt", "neu_")

# b) erneut prüfen
txt_dateien = listdir_filter("MeineDaten2", ".txt")
print("Nach dem Umbenennen:", txt_dateien)

# d)
personen = [
    {"name": "Max", "alter": 25},
    {"name": "Tom", "alter": 30}
]

json_speichern("personen.json", personen)

# e)
daten = json_laden("personen.json")
print("Geladene JSON-Daten:")
print(daten)

# f)
ergebnis = regex_suche("MeineDaten2", "Hallo")
print("Dateien mit Treffer:", ergebnis)