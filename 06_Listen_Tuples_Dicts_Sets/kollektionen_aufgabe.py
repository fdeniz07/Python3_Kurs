# kollektionen_aufgabe.py
import random

# a) Importiere random und erzeuge eine Liste von 10 zufälligen Ganzzahlen zwischen 1 und 100
zufallszahlen = [random.randint(1, 100) for _ in range(10)]
print(f"Ursprüngliche Liste: {zufallszahlen}\n")

# b) Funktion sortiere_und_zähle erstellen
def sortiere_und_zaehle(zahlen_liste):
    zahlen_liste.sort()          # Sortiert die übergebene Liste aufsteigend
    anzahl = len(zahlen_liste)   # Ermittelt die Anzahl der Elemente
    return anzahl

# Aufruf der Funktion mit unserer Zufallsliste
anzahl_elemente = sortiere_und_zaehle(zufallszahlen)
print(f"Sortierte Liste:     {zufallszahlen}")
print(f"Anzahl der Elemente: {anzahl_elemente}\n")

# c) Liste mit Tupeln aus (Zahl, Quadrat der Zahl) erstellen
quadrat_tupel = [(zahl, zahl**2) for zahl in zufallszahlen]

# d) Schleife über die Tupel-Liste mit formatierter Ausgabe
print("Quadratzahlen-Übersicht:")
for zahl, quadrat in quadrat_tupel:
    print(f"Die Zahl {zahl:2d} hat das Quadrat {quadrat:4d}")
print()

# e) Kontrollstruktur zur Überprüfung der Elementanzahl
if anzahl_elemente > 5:
    print("Mehr als 5 Elemente")
else:
    print("5 oder weniger Elemente")