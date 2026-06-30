import re
import json


# a) Feedback-Datei lesen
def lese_feedback(dateiname):
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            return datei.read()
    except FileNotFoundError:
        print("\u274C Fehler: Datei wurde nicht gefunden.")
        return None
    except IOError as fehler:
        print(f"\u274C I/O-Fehler: {fehler}")
        return None


# b) Datumsangaben extrahieren
def finde_daten(text):
    return re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)


# c) Datumsvorkommen zählen
def zaehle_daten(daten):
    datums_vorkommen = {}

    for datum in daten:
        if datum in datums_vorkommen:
            datums_vorkommen[datum] += 1
        else:
            datums_vorkommen[datum] = 1

    return datums_vorkommen


# d) Kommentare mit "exzellent" finden
def finde_exzellente_kommentare(text):
    kommentare = text.split("\n")

    return [
        kommentar for kommentar in kommentare
        if re.search(r"exzellent", kommentar, re.IGNORECASE)
    ]


# e) JSON speichern
def speichere_json(dateiname, daten):
    try:
        with open(dateiname, "w", encoding="utf-8") as datei:
            json.dump(daten, datei, indent=4, ensure_ascii=False)

        print(f"\u2705 {dateiname} wurde gespeichert.")

    except IOError as fehler:
        print(f"\u274C Fehler beim Speichern: {fehler}")


# Hauptprogramm
def main():

    text = lese_feedback("feedback.txt")

    if text is None:
        return

    daten = finde_daten(text)

    datums_vorkommen = zaehle_daten(daten)

    exzellente_kommentare = finde_exzellente_kommentare(text)

    speichere_json("datums_vorkommen.json", datums_vorkommen)
    speichere_json("exzellente_feedbacks.json", exzellente_kommentare)

    print("\n\U0001F389 Analyse erfolgreich abgeschlossen!")
    print(f"\U0001F4C5 Gefundene Datumsangaben: {len(daten)}")
    print(f"\U0001F4DD Exzellente Kommentare: {len(exzellente_kommentare)}")


if __name__ == "__main__":
    main()