# ------------------------------------------------------------
# Dateiname: gerade_zahlen_sortieren.py
# Gerade Zahlen filtern und mit Quicksort sortieren
#
# Entwickler: Fatih Deniz
# Erstelldatum: 09.07.2026
#
# Funktionen:
# - Gerade Zahlen aus einer Liste filtern
# - Liste mit Quicksort sortieren
# - Funktionen mit einer Testliste prüfen
# ------------------------------------------------------------

'''
Aufgabe: Fehler finden
Erstelle ein Python-Skript, das folgende Anforderungen erfüllt:

a) Definiere eine Funktion filtere_gerade_zahlen, die eine Liste von Zahlen als Argument nimmt und eine neue Liste zurückgibt, 
die nur die geraden Zahlen enthält. Verwende dazu eine Schleife, um durch die Liste zu iterieren.

b) Füge am Anfang der Funktion eine Zusicherung ein, die sicherstellt, dass das übergebene Argument eine Liste ist. 
Falls das Argument keine Liste ist, soll das Programm mit einer AssertionError enden.

c) Schreibe eine zweite Funktion sortiere_liste, die eine Liste von Zahlen nimmt und diese mit dem Quicksort-Algorithmus 
sortiert. Du kannst die Implementierung des Quicksort-Algorithmus selbst wählen, achte aber darauf, 
dass du den Algorithmus korrekt implementierst.

d) Verwende die Funktion filtere_gerade_zahlen, um eine Liste von Zahlen zu filtern, und verwende 
dann die Funktion sortiere_liste, um die gefilterte Liste zu sortieren. Gib das Ergebnis aus.

e) Füge am Ende des Skripts eine Testroutine ein, die deine Funktionen mit einer vorgegebenen Liste von Zahlen testet. 
Die Liste soll sowohl positive als auch negative Zahlen sowie Null enthalten. 
'''


def filtere_gerade_zahlen(zahlen):
    """Filtert alle geraden Zahlen aus einer Liste."""

    assert isinstance(zahlen, list), "Das Argument muss eine Liste sein."

    gerade_zahlen = []

    for zahl in zahlen:
        if zahl % 2 == 0:
            gerade_zahlen.append(zahl)

    return gerade_zahlen


def sortiere_liste(liste):
    """Sortiert eine Liste mit dem Quicksort-Algorithmus."""

    if len(liste) <= 1:
        return liste

    pivot = liste[0]

    kleiner = []
    gleich = []
    groesser = []

    for zahl in liste:
        if zahl < pivot:
            kleiner.append(zahl)
        elif zahl > pivot:
            groesser.append(zahl)
        else:
            gleich.append(zahl)

    return (
        sortiere_liste(kleiner)
        + gleich
        + sortiere_liste(groesser)
    )


# ------------------------------------------------------------
# Testroutine
# ------------------------------------------------------------

def main():
    zahlen = [12, -5, 8, 0, -10, 3, 17, 24, 0, 44, 21, -5, -2, 7]

    print("Originalliste:")
    print(zahlen)

    gerade = filtere_gerade_zahlen(zahlen)

    print("\nGerade Zahlen:")
    print(gerade)

    sortiert = sortiere_liste(gerade)

    print("\nSortierte gerade Zahlen:")
    print(sortiert)

if __name__ == "__main__":
    main()