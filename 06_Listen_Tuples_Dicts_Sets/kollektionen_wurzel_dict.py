# kollektionen_wurzel_dict.py

# a) Importiere die spezifischen Funktionen aus den Modulen random und math
from random import randint
from math import sqrt

# b) Funktion zur Generierung einer Liste von n Zufallszahlen zwischen 1 und 100
def erzeuge_zufallszahlen_liste(n):
    # Nutzt 'randint' und '_', da die Schleifenvariable nicht benötigt wird
    return [randint(1, 100) for _ in range(n)]

# c) Funktion zur Berechnung der Quadratwurzeln für jedes Element der Liste
def berechne_wurzeln(liste):
    # Berechnet für jede Zahl die Wurzel und rundet sie hier für eine schönere 
    # Ausgabe optional auf 2 Nachkommastellen (kann bei Bedarf entfernt werden)
    return [round(sqrt(zahl), 2) for zahl in liste]

# d) Funktion zum Sortieren und Erzeugen von (Originalzahl, Quadratwurzel)-Tupeln
def sortiere_und_erzeuge_tupel(liste):
    # Da in der Aufgabe steht, dass die Liste der *Quadratwurzeln* aufsteigend 
    # sortiert werden soll, berechnen wir die Wurzeln, sortieren sie und paaren 
    # sie mit ihren quadrierten Originalwerten zurück.
    
    wurzeln = berechne_wurzeln(liste)
    wurzeln.sort()  # Aufsteigend sortieren
    
    # Tupel-Liste erstellen: (Originalzahl, Quadratwurzel)
    # Hinweis: Da die Wurzeln sortiert sind, quadrieren wir sie zurück,
    # um die dazugehörige Originalzahl (gerundet als Integer) zu erhalten.
    tupel_liste = [(int(round(w**2)), w) for w in wurzeln]
    return tupel_liste

# e) Funktion zur Erstellung eines Dictionarys aus der Tupel-Liste
def erstelle_dictionary(tupel_liste):
    # dict() konvertiert eine Liste, die aus (Schlüssel, Wert)-Paaren besteht,
    # direkt in ein fertiges Python-Dictionary.
    return dict(tupel_liste)

# f) Hauptfunktion main(), die alle Schritte koordiniert
def main():
    # 1. Erzeuge eine Liste mit 10 zufälligen Zahlen
    original_liste = erzeuge_zufallszahlen_liste(10)
    print(f"1. Generierte Zufallszahlen:   {original_liste}")
    
    # 2. Berechne die Quadratwurzeln (separat zur Veranschaulichung für Teil c)
    wurzel_liste = berechne_wurzeln(original_liste)
    print(f"2. Berechnete Wurzeln:         {wurzel_liste}")
    
    # 3. Sortiere die Wurzeln und erzeuge die Tupel-Liste
    tupel_ergebnis = sortiere_and_erzeuge_tupel(original_liste)
    print(f"3. Sortierte Tupel-Liste:      {tupel_ergebnis}")
    
    # 4. Erstelle das finale Dictionary
    mein_wörterbuch = erstelle_dictionary(tupel_ergebnis)
    
    # g) Gib am Ende des Programms das erstellte Dictionary aus
    print("\ng) Das finale Dictionary (Schlüssel: Originalzahl -> Wert: Wurzel):")
    print(mein_wörterbuch)

# Startet das Programm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()