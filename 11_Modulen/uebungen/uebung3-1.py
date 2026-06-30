import re
import json


# a) Datei lesen
try:
    with open("feedback.txt", "r", encoding="utf-8") as datei:
        text = datei.read()

except FileNotFoundError:
    print("\u274C Die Datei wurde nicht gefunden.")
    exit()

except Exception as fehler:
    print("Fehler:", fehler)
    exit()


# b) Alle Datumsangaben finden
daten = re.findall(r"\d{2}\.\d{2}\.\d{4}", text)


# c) Datumsangaben zählen
datums_vorkommen = {}

for datum in daten:
    if datum in datums_vorkommen:
        datums_vorkommen[datum] += 1
    else:
        datums_vorkommen[datum] = 1


# d) Kommentare mit "exzellent" suchen
exzellente_kommentare = []

kommentare = text.split("\n")

for kommentar in kommentare:
    if re.search("exzellent", kommentar, re.IGNORECASE):
        exzellente_kommentare.append(kommentar)


# e) JSON-Dateien speichern
try:

    with open("datums_vorkommen.json", "w", encoding="utf-8") as datei:
        json.dump(datums_vorkommen, datei, indent=4, ensure_ascii=False)

    with open("exzellente_feedbacks.json", "w", encoding="utf-8") as datei:
        json.dump(exzellente_kommentare, datei, indent=4, ensure_ascii=False)

except Exception as fehler:
    print("Fehler beim Speichern:", fehler)


# g) Ausgabe
print("\u2705 Die Analyse wurde erfolgreich abgeschlossen.")
print("\U0001F389 Fertig!")