'''
Aufgabe: Textverarbeitung
Entwickle ein Python-Programm, das eine Textdatei mit einer Liste von Produkten und deren Preisen verarbeitet. 
Die Datei soll in folgendem Format vorliegen:

Produkt,Preis

Milch,1.29

Brot,2.49

Äpfel,3.19

a) Lese die Datei ein und speichere die Daten in einer geeigneten Datenstruktur. Verwende dabei die with-Anweisung und stelle sicher, 
dass Fehler beim Lesen der Datei ordnungsgemäß behandelt werden.

b) Füge eine Funktion hinzu, die die Mehrwertsteuer für jedes Produkt berechnet. Die Mehrwertsteuer beträgt 19%. 
Speichere die Ergebnisse in einer neuen Datenstruktur, die sowohl den Originalpreis als auch den Preis inklusive Mehrwertsteuer enthält.

c) Erweitere das Programm, sodass es eine neue Datei erstellt, die neben dem Produktnamen und dem Originalpreis 
auch den Preis inklusive Mehrwertsteuer enthält. Das Format soll wie folgt sein:

Produkt,Preis,MwSt

Milch,1.29,1.54

Brot,2.49,2.96

Äpfel,3.19,3.80

d) Implementiere eine Fehlerbehandlung für den Fall, dass die Eingabedatei Produkte mit ungültigen Preisen enthält (z.B. nicht-numerische Werte). 
In solchen Fällen soll eine Warnmeldung ausgegeben und das betroffene Produkt übersprungen werden.

e) Verwende reguläre Ausdrücke, um zu überprüfen, ob die Produktbezeichnungen gültig sind (bestehend aus Buchstaben, Zahlen und ggf. Leerzeichen). 
Ungültige Produktbezeichnungen sollen ähnlich wie bei d) behandelt werden. 
'''


import re
import csv

def verarbeite_preisliste(input_datei, output_datei):
    # Regex für gültige Produktbezeichnungen: Buchstaben, Zahlen, Leerzeichen
    produkt_pattern = re.compile(r'^[a-zA-Z0-9äöüÄÖÜß\s]+$')
    
    daten = []
    
    try:
        with open(input_datei, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for zeile in reader:
                produkt = zeile['Produkt']
                preis_str = zeile['Preis']
                
                # e) Validierung des Produktnamens mit Regex
                if not produkt_pattern.match(produkt):
                    print(f"Warnung: Ungültiger Produktname '{produkt}' wird übersprungen.")
                    continue
                
                # d) Fehlerbehandlung für nicht-numerische Preise
                try:
                    preis = float(preis_str)
                    
                    # b) Berechnung der Mehrwertsteuer
                    mwst_faktor = 1.19
                    preis_mit_mwst = round(preis * mwst_faktor, 2)
                    
                    daten.append({
                        'Produkt': produkt,
                        'Preis': preis,
                        'MwSt': preis_mit_mwst
                    })
                except ValueError:
                    print(f"Warnung: Ungültiger Preis für '{produkt}': '{preis_str}'. Überspringe.")
                    
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{input_datei}' wurde nicht gefunden.")
        return

    # c) Neue Datei mit erweiterten Daten erstellen
    try:
        with open(output_datei, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Produkt', 'Preis', 'MwSt'])
            writer.writeheader()
            writer.writerows(daten)
        print(f"Erfolgreich: Daten wurden in '{output_datei}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Schreiben der Datei: {e}")

# --- Programmstart ---
if __name__ == "__main__":
    verarbeite_preisliste('produkte.csv', 'produkte_mit_mwst.csv')