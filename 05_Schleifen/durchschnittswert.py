
def berechne_durchschnitt(zahlen_liste):
    # Leere Liste prüfen
    if len(zahlen_liste) == 0:
        return None

    summe = 0

    # Summe mit einer for-Schleife berechnen
    for zahl in zahlen_liste:
        summe += zahl

    durchschnitt = summe / len(zahlen_liste)
    return durchschnitt


# Liste von Zahlen definieren
zahlen = [10, 20, 30, 40, 50]

# Funktion aufrufen
ergebnis = berechne_durchschnitt(zahlen)

# Ergebnis ausgeben
if ergebnis is None:
    print("Die Liste ist leer. Es kann kein Durchschnitt berechnet werden.")
else:
    print(f"Der Durchschnitt der Zahlenliste beträgt: {ergebnis}")
