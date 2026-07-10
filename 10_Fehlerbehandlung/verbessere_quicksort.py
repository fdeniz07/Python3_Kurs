# ------------------------------------------------------------
# Dateiname: verbessere_quicksort.py
# Verbesserter Quicksort
#
# Entwickler: Fatih Deniz
# Erstelldatum: 09.07.2026
#
# Funktionen:
# - Prüft, ob eine Liste bereits sortiert ist
# - Sortiert eine Liste mit Quicksort
# - Debug-Ausgabe über die Konsole
# ------------------------------------------------------------

'''
Aufgabe: Fehler finden und vermeiden
Du sollst eine Python-Funktion namens verbessere_quicksort schreiben, die den Quicksort-Algorithmus implementiert
und zusätzlich eine Verbesserung beinhaltet: Bevor die eigentliche Sortierung beginnt, soll überprüft werden, 
ob die Liste bereits sortiert ist. Ist dies der Fall, gibt die Funktion die Liste direkt zurück, 
ohne den Quicksort-Algorithmus durchzuführen. Diese Überprüfung soll durch eine Zusicherung (assert) realisiert werden, 
die sicherstellt, dass die Funktion nur dann den Quicksort-Algorithmus ausführt, wenn die Liste nicht bereits sortiert ist. 
Implementiere außerdem eine einfache Debugging-Ausgabe, die den Zustand der Liste vor und nach der Sortierung 
in die Konsole schreibt, sofern die Umgebungsvariable DEBUG auf True gesetzt ist.
'''


DEBUG = True


def ist_sortiert(liste):
    """Prüft, ob die Liste bereits sortiert ist."""

    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False

    return True


def verbessere_quicksort(liste):
    """Sortiert eine Liste mit dem Quicksort-Algorithmus."""

    assert isinstance(liste, list), "Das Argument muss eine Liste sein."

    if DEBUG:
        print("Vor der Sortierung:", liste)

    # Liste ist bereits sortiert
    if ist_sortiert(liste):
        if DEBUG:
            print("Die Liste ist bereits sortiert.")
        return liste

    if len(liste) <= 1:
        return liste

    pivot = liste[0]

    kleiner = []
    gleich = []
    groesser = []

    for element in liste:
        if element < pivot:
            kleiner.append(element)
        elif element > pivot:
            groesser.append(element)
        else:
            gleich.append(element)

    sortierte_liste = (
        verbessere_quicksort(kleiner)
        + gleich
        + verbessere_quicksort(groesser)
    )

    if DEBUG:
        print("Nach der Sortierung:", sortierte_liste)

    return sortierte_liste


# ------------------------------------------------------------
# Testroutine
# ------------------------------------------------------------

zahlen = [9, 5, 1, 7, 3, 2, 8, 6, 4]

ergebnis = verbessere_quicksort(zahlen)

print("\nErgebnis:")
print(ergebnis)