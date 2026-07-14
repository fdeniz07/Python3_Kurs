"""Ein einfaches Bankkonto-Management-System für die Konsole."""

'''
Aufgabe: Objektorientierte Programmierung
Entwickle ein Python-Programm, das ein einfaches Bankkonto-Management-System simuliert. 
Das Programm soll folgende Funktionalitäten umfassen:

a) Definiere eine Klasse Bankkonto, die Attribute für den Kontoinhaber (inhaber), 
die Kontonummer (konto_nr), den aktuellen Kontostand (kontostand) und eine Liste 
der letzten zehn Transaktionen (transaktionen) enthält. Der Kontostand soll mit einem Anfangswert 
von 0 initialisiert werden, und die Liste der Transaktionen soll leer sein.

b) Implementiere eine Methode einzahlen, die einen Betrag annimmt und den Kontostand entsprechend erhöht. 
Die Methode soll außerdem die Transaktion (Datum, Uhrzeit, Betrag) in der Transaktionsliste speichern. 
Verwende das Modul datetime, um das aktuelle Datum und die Uhrzeit zu erfassen.

c) Implementiere eine Methode abheben, die einen Betrag annimmt und prüft, ob der Betrag vom aktuellen Kontostand 
abgehoben werden kann. Wenn ja, soll der Betrag abgehoben und die Transaktion gespeichert werden. Wenn nicht, 
soll eine Ausnahme mit der Nachricht "Nicht genügend Guthaben" geworfen werden.

d) Füge eine Methode letzte_transaktionen hinzu, die die letzten zehn Transaktionen anzeigt.

e) Erstelle eine Instanz der Klasse Bankkonto für einen Benutzer und führe verschiedene Einzahlungen 
und Abhebungen durch. Verwende Ausnahmen, um Fehler wie das Abheben eines Betrags, der den Kontostand übersteigt, 
zu behandeln.

f) Implementiere eine einfache Benutzeroberfläche in der Konsole, die es dem Benutzer ermöglicht, 
Einzahlungen und Abhebungen zu tätigen und die letzten Transaktionen einzusehen. 
'''



from datetime import datetime


class Bankkonto:
    """Repräsentiert ein Bankkonto mit den letzten zehn Transaktionen."""

    def __init__(self, inhaber, konto_nr):
        self.inhaber = inhaber
        self.konto_nr = konto_nr
        self.kontostand = 0.0
        self.transaktionen = []

    def _transaktion_speichern(self, art, betrag):
        """Speichert eine Transaktion und behält höchstens zehn Einträge."""
        zeitpunkt = datetime.now()
        self.transaktionen.append(
            {
                "datum": zeitpunkt.strftime("%d.%m.%Y"),
                "uhrzeit": zeitpunkt.strftime("%H:%M:%S"),
                "art": art,
                "betrag": betrag,
            }
        )

        # Die älteste Transaktion entfernen, sobald mehr als zehn vorhanden sind.
        if len(self.transaktionen) > 10:
            self.transaktionen.pop(0)

    @staticmethod
    def _betrag_pruefen(betrag):
        """Stellt sicher, dass ein positiver Betrag verarbeitet wird."""
        if betrag <= 0:
            raise ValueError("Der Betrag muss größer als 0 sein.")

    def einzahlen(self, betrag):
        """Erhöht den Kontostand um den eingezahlten Betrag."""
        self._betrag_pruefen(betrag)
        self.kontostand += betrag
        self._transaktion_speichern("Einzahlung", betrag)

    def abheben(self, betrag):
        """Hebt einen Betrag ab, sofern ausreichend Guthaben vorhanden ist."""
        self._betrag_pruefen(betrag)

        if betrag > self.kontostand:
            raise ValueError("Nicht genügend Guthaben")

        self.kontostand -= betrag
        self._transaktion_speichern("Abhebung", betrag)

    def letzte_transaktionen(self):
        """Gibt die gespeicherten Transaktionen formatiert in der Konsole aus."""
        if not self.transaktionen:
            print("Es wurden noch keine Transaktionen durchgeführt.")
            return

        print("\n--- Letzte Transaktionen ---")
        for transaktion in self.transaktionen:
            print(
                f"{transaktion['datum']} {transaktion['uhrzeit']} | "
                f"{transaktion['art']}: {transaktion['betrag']:.2f} €"
            )

    def kontoinformationen_anzeigen(self):
        """Zeigt die wichtigsten Daten des Kontos an."""
        print("\n--- Kontoinformationen ---")
        print(f"Inhaber: {self.inhaber}")
        print(f"Kontonummer: {self.konto_nr}")
        print(f"Kontostand: {self.kontostand:.2f} €")


def betrag_eingeben():
    """Liest einen Betrag ein und akzeptiert Komma oder Punkt als Trennzeichen."""
    eingabe = input("Betrag eingeben: ").replace(",", ".")
    return float(eingabe)


def menue_anzeigen():
    """Zeigt die verfügbaren Aktionen der Konsolenoberfläche an."""
    print("\n--- Bankkonto-Management ---")
    print("1 - Einzahlen")
    print("2 - Abheben")
    print("3 - Letzte Transaktionen anzeigen")
    print("4 - Kontoinformationen anzeigen")
    print("0 - Programm beenden")


def main():
    """Startet die einfache Konsolenoberfläche für ein Bankkonto."""
    print("Willkommen beim Bankkonto-Management-System!")
    inhaber = input("Name des Kontoinhabers: ")
    konto_nr = input("Kontonummer: ")
    konto = Bankkonto(inhaber, konto_nr)

    while True:
        menue_anzeigen()
        auswahl = input("Bitte wählen Sie eine Aktion: ")

        try:
            if auswahl == "1":
                konto.einzahlen(betrag_eingeben())
                print(f"Einzahlung erfolgreich. Neuer Kontostand: {konto.kontostand:.2f} €")
            elif auswahl == "2":
                konto.abheben(betrag_eingeben())
                print(f"Abhebung erfolgreich. Neuer Kontostand: {konto.kontostand:.2f} €")
            elif auswahl == "3":
                konto.letzte_transaktionen()
            elif auswahl == "4":
                konto.kontoinformationen_anzeigen()
            elif auswahl == "0":
                print("Auf Wiedersehen!")
                break
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Zahl aus dem Menü.")
        except ValueError as fehler:
            print(f"Fehler: {fehler}")


if __name__ == "__main__":
    main()
