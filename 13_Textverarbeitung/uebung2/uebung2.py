'''
Aufgabe: Textverarbeitung
Entwickle ein Python-Skript, das folgende Aufgaben erfüllt:

a) Lese eine Textdatei namens "tagebuch.txt", die in UTF-8 kodiert ist, und speichere den Inhalt in einer Variablen. 
Verwende die with-answeisung und try-except-Blöcke, um Fehler beim Dateizugriff zu handhaben.

b) Verwende eine Funktion, um alle Vorkommen eines bestimmten Wortes im Text zu zählen. 
Das Wort soll als Parameter an die Funktion übergeben werden.

c) Ersetze in dem Text alle Vorkommen des Wortes "traurig" durch "glücklich" 
und speichere das Ergebnis in einer neuen Datei namens "tagebuch_neu.txt".

d) Schreibe eine weitere Funktion, die den aktualisierten Text nimmt und eine Liste von Sätzen zurückgibt, 
wobei jeder Satz ein Element der Liste ist. Verwende dazu eine geeignete String-Methode.

e) Konvertiere die Liste von Sätzen in ein JSON-Format und speichere diese Daten in einer Datei namens "tagebuch_saetze.json".

Stelle sicher, dass dein Skript modular aufgebaut ist und du Import-Module für JSON-Funktionalitäten
und andere benötigte Funktionen verwendest. 
'''


import json

def lese_datei(dateiname):
    """a) Datei lesen mit Fehlerbehandlung."""
    try:
        with open(dateiname, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return None

def zaehle_wort(text, wort):
    """b) Vorkommen eines Wortes zählen."""
    # Wir teilen den Text in Wörter auf, um genaue Treffer zu erhalten
    woerter = text.replace(".", "").replace(",", "").split() # Punkt und Komma entfernen, um saubere Wörter zu erhalten
    return woerter.count(wort) # Anzahl der Vorkommen des Wortes zurückgeben

def verarbeite_und_speichere(text, input_datei, output_datei):
    """c) 'traurig' durch 'glücklich' ersetzen und speichern."""
    neuer_text = text.replace("traurig", "glücklich")
    try:
        with open(output_datei, "w", encoding="utf-8") as file: 
            file.write(neuer_text)
        print(f"Datei erfolgreich als '{output_datei}' gespeichert.")
        return neuer_text
    except IOError as e:
        print(f"Fehler beim Schreiben: {e}")
        return text

def extrahiere_saetze(text):
    """d) Text in eine Liste von Sätzen zerlegen."""
    # Einfache Zerlegung bei '.' (kann bei Bedarf komplexer gestaltet werden)
    return [satz.strip() for satz in text.split('.') if satz.strip()] # Liste der Sätze zurückgeben, leere Sätze entfernen

def speichere_als_json(saetze, dateiname):
    """e) Liste von Sätzen als JSON speichern."""
    try:
        with open(dateiname, "w", encoding="utf-8") as file:
            json.dump(saetze, file, indent=4, ensure_ascii=False)
        print(f"Sätze erfolgreich in '{dateiname}' gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der JSON-Datei: {e}")

# --- Hauptprogramm ---
if __name__ == "__main__":
    datei = "tagebuch.txt"
    
    # a) Lesen
    inhalt = lese_datei(datei)
    
    if inhalt:
        # b) Zählen
        anzahl = zaehle_wort(inhalt, "traurig")
        print(f"Das Wort 'traurig' kommt {anzahl} Mal vor.")
        
        # c) Ersetzen und speichern
        aktualisierter_text = verarbeite_und_speichere(inhalt, datei, "tagebuch_neu.txt")
        
        # d) Sätze extrahieren
        saetze_liste = extrahiere_saetze(aktualisierter_text)
        
        # e) JSON speichern
        speichere_als_json(saetze_liste, "tagebuch_saetze.json")