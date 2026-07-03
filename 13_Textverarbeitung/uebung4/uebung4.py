'''
Aufgabe: Textverarbeitung
Erstelle ein Python-Skript, das folgende Aufgaben erfüllt:

a) Definiere eine Variable text, die einen mehrzeiligen String speichert, welcher Sonderzeichen und Unicode-Zeichen enthält. 
Verwende mindestens drei verschiedene Escape-Sequenzen und zwei Unicode-Zeichen (z.B. ein Emoji und ein Zeichen aus einem anderen Schriftsystem).

b) Zähle, wie oft ein bestimmtes Wort in text vorkommt. Das Wort soll als Eingabe über die Konsole gegeben werden.

c) Ersetze in text alle Vorkommen eines bestimmten Wortes (ebenfalls über die Konsole eingegeben) 
durch ein anderes Wort (auch über die Konsole eingegeben) und gib den neuen Text aus.

d) Speichere den modifizierten Text in einer Datei mit dem Namen modifizierter_text.txt unter Verwendung der with-Anweisung.

e) Dies eine Datei namens daten.json, die eine Liste von Dictionaries enthält, ein. Verwende das JSON-Modul, 
um die Datei zu laden. Gib anschließend die Daten in der Konsole aus. 
'''


import json
import os

# a) Mehrzeiliger String mit Escape-Sequenzen und Unicode
# \n = Zeilenumbruch, \" = Anführungszeichen, \\ = Backslash
# \U0001F600 = Emoji, \u99ac = Chinesisches Schriftzeichen
text = (
    "Hallo! \"Willkommen\" bei Python.\n"
    "Das ist ein Backslash: \\ und ein Emoji: \U0001F600.\n"
    "Hier ist ein Zeichen aus China: \u99ac."
)

def wort_zaehlen(t, wort):
    """b) Zählt die Vorkommen eines Wortes."""
    # Wir teilen den Text an Leerzeichen, um exakte Worttreffer zu finden
    woerter = t.lower().split()
    return woerter.count(wort.lower())

def text_ersetzen(t, alt, neu):
    """c) Ersetzt Wörter im Text."""
    return t.replace(alt, neu)

def speichere_text(t, dateiname):
    """d) Speichert Text mit with-Anweisung."""
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write(t)
    print(f"Text wurde erfolgreich in '{dateiname}' gespeichert.")

def json_datei_lesen(dateiname):
    """e) Lädt und liest eine JSON-Datei."""
    if not os.path.exists(dateiname):
        print(f"Datei {dateiname} nicht gefunden.")
        return

    with open(dateiname, "r", encoding="utf-8") as f:
        daten = json.load(f)
        print("\n--- Inhalt der JSON-Datei ---")
        for eintrag in daten:
            print(eintrag)

# --- Hauptprogramm ---
if __name__ == "__main__":
    print("Originaler Text:")
    print(text)
    
    # b) Wort zählen
    such_wort = input("\nWelches Wort möchtest du zählen? ")
    anzahl = wort_zaehlen(text, such_wort)
    print(f"Das Wort '{such_wort}' kommt {anzahl} Mal vor.")
    
    # c) Wort ersetzen
    altes_wort = input("\nWelches Wort soll ersetzt werden? ")
    neues_wort = input("Durch welches Wort soll es ersetzt werden? ")
    neuer_text = text_ersetzen(text, altes_wort, neues_wort)
    print("\nNeuer Text:")
    print(neuer_text)
    
    # d) Speichern
    speichere_text(neuer_text, "modifizierter_text.txt")
    
    # e) JSON lesen (Stelle sicher, dass 'daten.json' existiert)
    json_datei_lesen("daten.json")