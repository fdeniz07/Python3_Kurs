import datetime


class Bankkonto:
    def __init__(self, inhaber, konto_nr):
        self.inhaber = inhaber
        self.konto_nr = konto_nr
        self.kontostand = 0
        self.transaktionen = []


    def einzahlen(self, betrag):
        self.kontostand += betrag
        self.transaktionen.append((datetime.datetime.now(), "Einzahlung", betrag))
        self.transaktionen = self.transaktionen[-10:]  # Behalte nur die letzten 10 Transaktionen


    def abheben(self, betrag):
        if self.kontostand >= betrag:
            self.kontostand -= betrag
            self.transaktionen.append((datetime.datetime.now(), "Abhebung", betrag))
            self.transaktionen = self.transaktionen[-10:]
        else:
            raise ValueError("Nicht genügend Guthaben")


    def letzte_transaktionen(self):
        for datum, typ, betrag in self.transaktionen:
            print(f"{datum}: {typ} von {betrag}€")


def main():
    konto = Bankkonto("Max Mustermann", "DE1234567890")
    while True:
        aktion = input("Wählen Sie eine Aktion: (E)inzahlen, (A)bheben, (T)ransaktionen anzeigen, (B)eenden: ").upper()
        if aktion == "E":
            betrag = float(input("Betrag zum Einzahlen: "))
            konto.einzahlen(betrag)
            print(f"{betrag}€ wurden eingezahlt.")
        elif aktion == "A":
            betrag = float(input("Betrag zum Abheben: "))
            try:
                konto.abheben(betrag)
                print(f"{betrag}€ wurden abgehoben.")
            except ValueError as e:
                print(e)
        elif aktion == "T":
            konto.letzte_transaktionen()
        elif aktion == "B":
            break
        else:
            print("Ungültige Aktion.")


if __name__ == "__main__":
    main()
