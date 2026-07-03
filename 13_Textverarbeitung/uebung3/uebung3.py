'''
Aufgabe: Textverarbeitung
Entwickle ein Python-Programm, das folgende Funktionalitäten umfasst:

a) Lese einen Text aus einer Datei, die Unicode-Zeichen enthält, und speichere den Text in einer Variablen. 
Verwende dazu die with-Anweisung und stelle sicher, dass die Datei korrekt geschlossen wird.

b) Verwende reguläre Ausdrücke, um alle Wörter im Text zu finden, die mit einem Großbuchstaben beginnen, 
und speichere diese Wörter in einer Liste.

c) Erstelle eine Funktion, die die Anzahl der Vorkommen jedes Wortes in der Liste aus b) zählt und diese in einem Dictionary speichert.

d) Speichere das Dictionary aus c) in einer JSON-Datei. Stelle sicher, dass Umlaute und Sonderzeichen korrekt gespeichert werden.

e) Lies die JSON-Datei, die du in d) erstellt hast, und gib den Inhalt in der Konsole aus. 
Verwende hierbei die richtige Kodierung, um Umlaute und Sonderzeichen korrekt darzustellen. 

'''

import re
import json

# --- a) Datei lesen mit with-Anweisung ---
def lese_text_datei(dateiname):
    try:
        with open(dateiname, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
        return None

# --- b) Reguläre Ausdrücke nutzen ---
def finde_grossgeschriebene_woerter(text):
    # \b ist eine Wortgrenze, [A-Z] sucht Großbuchstaben, \w* den Rest des Wortes
    pattern = r'\b[A-ZÄÖÜ]\w*' #r'\b[A-ZÄÖÜ][a-zäöüß]*'
    return re.findall(pattern, text)

# --- c) Wörter zählen und Dictionary erstellen ---
def zaehle_woerter(woerter_liste):
    wort_count = {}
    for wort in woerter_liste:
        wort_count[wort] = wort_count.get(wort, 0) + 1
    return wort_count

# --- d) JSON speichern ---
def speichere_json(daten, dateiname):
    try:
        with open(dateiname, "w", encoding="utf-8") as file:
            # ensure_ascii=False sorgt dafür, dass Umlaute korrekt gespeichert werden
            json.dump(daten, file, indent=4, ensure_ascii=False)
        print(f"Daten erfolgreich in '{dateiname}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern: {e}")

# --- e) JSON lesen und ausgeben ---
def lese_json(dateiname):
    try:
        with open(dateiname, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Fehler beim Lesen der JSON: {e}")
        return None

# --- Hauptprogramm ---
if __name__ == "__main__":
    datei = "beispiel.txt"
    json_datei = "wort_statistik.json"
    
    # a) Datei einlesen
    inhalt = lese_text_datei(datei)
    
    if inhalt:
        # b) Wörter finden
        gross_woerter = finde_grossgeschriebene_woerter(inhalt)
        
        # c) Wörter zählen
        statistik = zaehle_woerter(gross_woerter)
        
        # d) JSON speichern
        speichere_json(statistik, json_datei)
        
        # e) JSON wieder einlesen und ausgeben
        ergebnis = lese_json(json_datei)
        if ergebnis:
            print("\n--- Wort-Statistik aus JSON ---")
            for wort, anzahl in ergebnis.items():
                print(f"{wort}: {anzahl}")