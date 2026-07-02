'''
Aufgabe: Textverarbeitung
Erstelle ein Python-Skript, das folgende Aufgaben ausführt:

a) Definiere eine Variable text, die einen mehrzeiligen String speichert. 
Der String soll mindestens ein Unicode-Zeichen, eine Escape-Sequenz und variable Teile enthalten, 
die durch die format() Methode ersetzt werden. 
Verwende für das Unicode-Zeichen ein Emoji und für die Escape-Sequenz einen Zeilenumbruch.

b) Verwende die print() Funktion, um den String auszugeben.

c) Lese eine Textdatei namens beispiel.txt, die du zuvor selbst erstellen musst, mit der with-Anweisung und utf-8 Encoding. 
Speichere den Inhalt der Datei in einer Variablen und gib ihn aus.

d) Schreibe eine Funktion speichere_json, die ein Python-Objekt (z.B. ein Dictionary mit einigen Schlüssel-Wert-Paaren) 
in eine Datei im JSON-Format speichert. Verwende dazu das Modul json.
'''
# -----------------------------------------------------------------------------------------------------------------------------

import json
import os

# --- a) Mehrzeiliger String mit Unicode, Escape-Sequenz und format() ---
# \n ist der Zeilenumbruch, \U0001F600 ist ein lächelndes Emoji
text = "Hallo {name}!\nHier ist ein Unicode-Zeichen: \U0001F600\nWillkommen zu deinem {thema}."
variable_text = text.format(name="Entwickler", thema="Python-Kurs")

# --- b) Ausgabe des Strings ---
print("--- Aufgabe b: String-Ausgabe ---")
print(variable_text)
print("-" * 50)

# --- c) & e) Datei lesen mit with, utf-8 und Fehlerbehandlung ---
def lese_datei(dateiname):
    print(f"\n--- Aufgabe c & e: Datei lesen '{dateiname}' ---")
    try:
        with open(dateiname, "r", encoding="utf-8") as file:
            inhalt = file.read()
            print("Dateiinhalt:")
            print(inhalt)
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden. Bitte erstelle sie!")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# --- d) JSON speichern ---
def speichere_json(daten, dateiname):
    print(f"\n--- Aufgabe d: JSON speichern in '{dateiname}' ---")
    try:
        with open(dateiname, "w", encoding="utf-8") as file:
            json.dump(daten, file, indent=4, ensure_ascii=False)
        print("Daten erfolgreich im JSON-Format gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern: {e}")
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden. Bitte erstelle sie!")

# --- Ausführung ---
if __name__ == "__main__":
    # Datei-Operationen ausführen
    lese_datei("beispiel.txt")
    
    # Beispiel-Daten für JSON
    mein_dict = {
        "Projekt": "Textverarbeitung",
        "Status": "Erfolgreich",
        "Wichtigkeit": 1
    }
    speichere_json(mein_dict, "daten.json")