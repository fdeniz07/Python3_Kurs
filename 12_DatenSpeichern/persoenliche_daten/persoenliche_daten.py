
'''
Aufgabe: Daten speichern
Erstelle ein Python-Skript, das folgende Aufgaben erfüllt:

a) Definiere eine Variable alter und weise ihr dein Alter als Ganzzahl zu.

b) Definiere eine Liste hobbies mit mindestens drei deiner Hobbies als Strings.

c) Definiere ein Tupel lieblingsfarben mit mindestens drei deiner Lieblingsfarben als Strings.

d) Schreibe eine Schleife, die für jedes Hobby in hobbies ausgibt: "Eines meiner Hobbies ist: [Hobby]."

e) Definiere eine Funktion jahre_bis_rente, die das Alter als Parameter annimmt und berechnet, wie viele Jahre du bis zur Rente (angenommen mit 65 Jahren) hast. Die Funktion soll das Ergebnis zurückgeben.

f) Importiere das Modul json und speichere die Daten aus hobbies und lieblingsfarben in einem Dictionary mit den Schlüsseln "Hobbies" und "Lieblingsfarben" in einer JSON-Datei namens persoenliche_daten.json.

g) Verwende eine try-except-Block, um die Datei zu öffnen und sicherzustellen, dass eine Nachricht "Fehler beim Speichern der Daten" ausgegeben wird, falls ein Fehler auftritt.

h) Verwende die with-Anweisung, um sicherzustellen, dass die Datei korrekt geschlossen wird, nachdem der Schreibvorgang abgeschlossen oder ein Fehler aufgetreten ist. 
'''

import json

DATEI_PFAD = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\persoenliche_daten\\persoenliche_daten.json"

# a) Variable alter
alter = 25 

# b) Liste hobbies
hobbies = ["Programmieren", "Wandern", "Fotografie"]

# c) Tupel lieblingsfarben
lieblingsfarben = ("Blau", "Grün", "Schwarz")

# d) Schleife für Hobbies
for hobby in hobbies:
    print(f"Eines meiner Hobbies ist: {hobby}.")

# e) Funktion jahre_bis_rente
def jahre_bis_rente(aktuelles_alter):
    rente_alter = 65
    return rente_alter - aktuelles_alter

# f) Dictionary für JSON erstellen
persoenliche_daten = {
    "Hobbies": hobbies,
    "Lieblingsfarben": list(lieblingsfarben) # JSON unterstützt keine Tupel direkt, daher in Liste konvertieren
}

# g) & h) Speichern in JSON mit with-Anweisung und Fehlerbehandlung
try:
    with open(DATEI_PFAD, "w", encoding="utf-8") as file:
        json.dump(persoenliche_daten, file, indent=4)
    print("\nDaten wurden erfolgreich in 'persoenliche_daten.json' gespeichert.")
except Exception:
    print("Fehler beim Speichern der Daten")

# Berechnung ausgeben
print(f"\nJahre bis zur Rente: {jahre_bis_rente(alter)} Jahre.")