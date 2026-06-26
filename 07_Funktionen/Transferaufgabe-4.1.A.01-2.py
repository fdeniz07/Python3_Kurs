# --------------------------------------------------
# Datentypen und Kontrollstrukturen
# Autor: Fatih Deniz
# --------------------------------------------------

# a) Liste von Tupeln erstellen
# Jedes Tupel besteht aus einem Buchstaben und einer Zahl.

elemente = [
    ("A", 1),
    ("B", 2),
    ("C", 3),
    ("D", 4),
    ("E", 5)
]


# --------------------------------------------------
# b) Funktion zum Suchen eines Elements
# Die Funktion überprüft, ob ein Tupel in der Liste
# vorhanden ist.
# --------------------------------------------------
def element_suchen(buchstabe, zahl):
    tupel = (buchstabe, zahl)

    if tupel in elemente:
        print(f"Element gefunden: {tupel}")
    else:
        print("Element nicht gefunden")


# --------------------------------------------------
# c) Funktion zum Umwandeln einer Zeichenkette
# in eine ganze Zahl (Typecasting)
# --------------------------------------------------
def string_zu_int(text):

    try:
        zahl = int(text)

        print(f"Umgewandelte Zahl: {zahl}")

        # --------------------------------------------------
        # f) Kontrollstruktur zur Überprüfung
        # ob die Zahl positiv, negativ oder Null ist
        # --------------------------------------------------
        if zahl > 0:
            print("Die Zahl ist positiv.")
        elif zahl < 0:
            print("Die Zahl ist negativ.")
        else:
            print("Die Zahl ist Null.")

    except ValueError:
        print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")


# --------------------------------------------------
# e) Einfache Benutzerschnittstelle
# Der Benutzer kann auswählen, welche Funktion
# getestet werden soll.
# --------------------------------------------------
while True:

    print("\n===== MENÜ =====")
    print("1 - Element suchen")
    print("2 - Zeichenkette in Zahl umwandeln")
    print("3 - Programm beenden")

    auswahl = input("Bitte wählen Sie eine Option: ")

    if auswahl == "1":

        buchstabe = input("Buchstabe eingeben: ")
        zahl = int(input("Zahl eingeben: "))

        element_suchen(buchstabe, zahl)

    elif auswahl == "2":

        text = input("Bitte geben Sie eine Zahl als Zeichenkette ein: ")
        string_zu_int(text)

    elif auswahl == "3":

        print("Programm wird beendet.")
        break

    else:
        print("Ungültige Auswahl.")

