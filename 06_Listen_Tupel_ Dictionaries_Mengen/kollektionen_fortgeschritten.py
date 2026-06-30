# kollektionen_fortgeschritten.py
# a) Importiere das Modul random und das Modul math
import random
import math

# b) Funktion zur Generierung der Zufallszahlenliste
def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    # Generiert eine Liste mit 'anzahl' Elementen zwischen 1 und max_wert (inklusive)
    return [random.randint(1, max_wert) for _ in range(anzahl)]

# c) Funktion zur Berechnung des Durchschnitts
def berechne_durchschnitt(zahlen_liste):
    if not zahlen_liste:  # Schutz vor Division durch Null, falls Liste leer ist
        return 0
    return sum(zahlen_liste) / len(zahlen_liste)

# d) Funktion zum Sortieren und Teilen der Liste
def sortiere_und_teile(zahlen_liste):
    # Zuerst die Liste aufsteigend sortieren
    zahlen_liste.sort()
    
    # Länge der Liste ermitteln
    laenge = len(zahlen_liste)
    
    # Den mathematischen Mittelpunkt berechnen.
    # math.ceil sorgt dafür, dass bei ungeraden Längen (z.B. 11 / 2 = 5.5 -> 6)
    # das mittlere Element zur ersten Hälfte wandert.
    mitte = math.ceil(laenge / 2)
    
    # Liste mithilfe von Slicing aufteilen
    erste_haelfte = zahlen_liste[:mitte]
    zweite_haelfte = zahlen_liste[mitte:]
    
    return erste_haelfte, zweite_haelfte

# ==========================================
# Hauptprogramm zur Ausführung (Anforderungen e - h)
# ==========================================

# e) Erzeuge eine Liste mit 10 Zufallszahlen bis max_wert 100
meine_liste = erzeuge_zufallszahlen_liste(10, 100)

# f) Gib die erzeugte Liste aus
print(f"f) Erzeugte Zufallsliste:             {meine_liste}")

# g) Berechne und gib den Durchschnittswert aus
durchschnitt = berechne_durchschnitt(meine_liste)
print(f"g) Durchschnittswert der Liste:       {durchschnitt:.2f}")

# h) Sortiere und teile die Liste, dann gib beide Hälften aus
erste, zweite = sortiere_und_teile(meine_liste)
print(f"h) Sortierte 1. Hälfte (inkl. Mitte): {erste}")
print(f"   Sortierte 2. Hälfte:               {zweite}")