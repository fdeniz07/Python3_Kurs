"""Einfache objektorientierte Simulation eines Online-Buchladens."""


class Buch:
    """Repräsentiert ein Buch im Inventar eines Buchladens."""

    def __init__(self, titel, autor, kategorie, preis):
        if preis < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")

        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = float(preis)

    def __str__(self):
        """Gibt das Buch in einer gut lesbaren Form zurück."""
        return (
            f"{self.titel} von {self.autor} "
            f"({self.kategorie}, {self.preis:.2f} €)"
        )


class Buchladen:
    """Verwaltet das Inventar und einfache Buchauswahlen."""

    def __init__(self):
        self.inventar = []

    def buch_hinzufuegen(self, buch):
        """Fügt ein Buch zum Inventar hinzu."""
        if not isinstance(buch, Buch):
            raise TypeError("Es können nur Buch-Objekte hinzugefügt werden.")
        self.inventar.append(buch)

    def nach_kategorie_suchen(self, kategorie):
        """Gibt alle Bücher der gewünschten Kategorie zurück."""
        return [
            buch
            for buch in self.inventar
            if buch.kategorie.casefold() == kategorie.casefold()
        ]

    def gesamtpreis_berechnen(self, buchauswahl):
        """Berechnet den Gesamtpreis einer Liste von Büchern."""
        if not all(isinstance(buch, Buch) for buch in buchauswahl):
            raise TypeError("Die Buchauswahl darf nur Buch-Objekte enthalten.")
        return sum(buch.preis for buch in buchauswahl)


def main():
    """Erstellt Beispieldaten und demonstriert die Klassenfunktionen."""
    buchladen = Buchladen()

    die_verwandlung = Buch("Die Verwandlung", "Franz Kafka", "Roman", 9.90)
    eine_kurze_geschichte_der_menschheit = Buch(
        "Eine kurze Geschichte der Menschheit", "Yuval Noah Harari", "Sachbuch", 16.00
    )
    das_universum = Buch("Das Universum", "Stephen Hawking", "Wissenschaft", 18.50)
    der_prozess = Buch("Der Prozess", "Franz Kafka", "Roman", 11.50)

    for buch in [
        die_verwandlung,
        eine_kurze_geschichte_der_menschheit,
        das_universum,
        der_prozess,
    ]:
        buchladen.buch_hinzufuegen(buch)

    print("--- Bücher der Kategorie Roman ---")
    romane = buchladen.nach_kategorie_suchen("Roman")
    for roman in romane:
        print(roman)

    auswahl = [die_verwandlung, das_universum]
    gesamtpreis = buchladen.gesamtpreis_berechnen(auswahl)
    print("\n--- Buchauswahl ---")
    for buch in auswahl:
        print(buch)
    print(f"Gesamtpreis: {gesamtpreis:.2f} €")


if __name__ == "__main__":
    main()
