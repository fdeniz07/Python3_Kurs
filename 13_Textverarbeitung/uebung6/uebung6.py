'''
Aufgabe: Textverarbeitung
Erstelle ein Python-Programm, das folgende Aufgaben erfüllt:

a) Definiere eine Variable, die einen Text in Form eines Strings speichert. 
Dieser Text soll mindestens ein Unicode-Zeichen enthalten, welches nicht auf einer normalen Tastatur zu finden ist. 
Verwende dazu die Funktion chr() mit einer Unicode-Nummer deiner Wahl.

b) Füge dem Text eine Escape-Sequenz hinzu, die einen Zeilenumbruch darstellt.

c) Verwende eine Stringmethode, um zu zählen, wie oft ein bestimmtes Zeichen in deinem Text vorkommt.

d) Erstelle eine Liste mit mehreren Strings. Verwende die Methode .join(), um einen neuen String zu erstellen, 
der die Elemente der Liste durch ein Komma getrennt enthält.

e) Speichere den Text aus a) in einer Datei. Verwende dazu die with-Anweisung und den Modus 'w' für das Schreiben in Dateien.

f) Lies den Text aus der Datei, die du in e) erstellt hast, und gib ihn auf der Konsole aus. 
Verwende dazu ebenfalls die with-Anweisung, diesmal mit dem Modus 'r' für das Lesen aus Dateien.

g) Fange mögliche Ausnahmen, die beim Lesen der Datei auftreten können, mit try und except ab.

h) Verwende das JSON-Format, um eine einfache Datenstruktur (z.B. ein Dictionary mit einigen Schlüssel-Wert-Paaren) 
in einer Datei zu speichern und wieder zu laden. 
'''


import json

# a) Variable mit Unicode-Zeichen über chr() und Unicode-Nummer
# \u2602 ist ein Regenschirm (Unicode-Nummer 9730)
unicode_zeichen = chr(9730) # Regenschirm symbol
text = f"Heute regnet es nicht {unicode_zeichen}. Es ist ein schöner Tag."

# b) Escape-Sequenz für Zeilenumbruch hinzufügen
text += "\nIch hoffe, du hattest einen guten Start in den Tag."

# c) Stringmethode zum Zählen (z.B. wie oft 'e' vorkommt)
anzahl_e = text.count('e')
print(f"Das Zeichen 'e' kommt {anzahl_e} Mal vor.")

# d) Liste erstellen und .join() verwenden
woerter_liste = ["Apfel", "Banane", "Kirsche"]
komma_string = ", ".join(woerter_liste)
print(f"Liste als String: {komma_string}")

# e) Text in Datei speichern (with-Anweisung, Modus 'w')
dateiname = "text_datei.txt"
with open(dateiname, "w", encoding="utf-8") as file:
    file.write(text)

# f) & g) Lesen der Datei mit try-except zur Fehlerbehandlung
try:
    with open(dateiname, "r", encoding="utf-8") as file:
        gelesener_text = file.read()
        print("\n--- Gelesener Text aus Datei ---")
        print(gelesener_text)
except FileNotFoundError:
    print("Fehler: Die Datei konnte nicht gefunden werden.")
except IOError:
    print("Fehler: Ein Problem ist beim Lesen der Datei aufgetreten.")

# h) JSON-Datenstruktur speichern und laden
daten = {"Name": "Python", "Typ": "Sprache", "Vielseitig": True}
json_datei = "daten.json"

# Speichern
with open(json_datei, "w", encoding="utf-8") as jf:
    json.dump(daten, jf, indent=4)

# Laden
try:
    with open(json_datei, "r", encoding="utf-8") as jf:
        geladene_daten = json.load(jf)
        print("\n--- Geladene JSON-Daten ---")
        print(geladene_daten)
except FileNotFoundError:
    print("Fehler: Die JSON-Datei konnte nicht gefunden werden.")
except json.JSONDecodeError:
    print("Fehler: Die JSON-Datei ist beschädigt oder entspricht nicht dem erwarteten Format.")