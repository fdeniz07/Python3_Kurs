def filtere_gerade_zahlen(zahlenliste):
    return list(filter(lambda zahl: zahl % 2 == 0, zahlenliste))


# Testliste
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Funktion aufrufen
gerade_zahlen = filtere_gerade_zahlen(zahlen)

# Ergebnis ausgeben
print("Gerade Zahlen:", gerade_zahlen)
