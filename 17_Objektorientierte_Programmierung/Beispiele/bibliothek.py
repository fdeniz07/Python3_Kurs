'''
Aufgabe: Objektorientierte Programmierung
Entwickle eine Python-Klasse namens Buch, die zur Verwaltung einer kleinen Bibliothek dient. 
Die Klasse soll folgende Attribute und Methoden haben:

a) Die Klasse soll drei Attribute haben: titel (String), autor (String) und ausgeliehen (Boolean), 
wobei ausgeliehen standardmäßig auf False gesetzt ist.

b) Schreibe eine Initialisierungsmethode __init__, die titel und autor als Parameter erhält und 
diese zusammen mit dem Standardwert für ausgeliehen setzt.

c) Füge eine Methode ausleihen hinzu, die das Attribut ausgeliehen auf True setzt, falls das Buch nicht bereits ausgeliehen ist. 
Falls das Buch bereits ausgeliehen ist, soll eine Nachricht "Buch bereits ausgeliehen" ausgegeben werden.

d) Füge eine Methode zurueckgeben hinzu, die das Attribut ausgeliehen auf False setzt, falls das Buch ausgeliehen war. 
Falls das Buch nicht ausgeliehen ist, soll eine Nachricht "Buch war nicht ausgeliehen" ausgegeben werden.

e) Schreibe eine Methode status, die den Titel, Autor und den Ausleihstatus des Buches in einem Satz ausgibt. 
'''


class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor
        self.ausgeliehen = False

    def ausleihen(self):
        if not self.ausgeliehen:
            self.ausgeliehen = True
        else:
            print(f"\nDas Buch '{self.titel}' von {self.autor} wurde ausgeliehen.")

    def zurueckgeben(self):
        if self.ausgeliehen:
            self.ausgeliehen = False
            print(f"\nDas Buch '{self.titel}' von {self.autor} wurde zurückgegeben.")
        else:
            print("\nBuch war nicht ausgeliehen")

    def status(self):
        if self.ausgeliehen:
            status = "ausgeliehen"
          # print(f"Das Buch '{self.titel}' von {self.autor} ist ausgeliehen.")
        else:
            status = "verfügbar"
          # print(f"Das Buch '{self.titel}' von {self.autor} ist verfügbar.")

        print(f"-->'{self.titel}' von {self.autor} ist {status}.")


# Bücher erstellen
print("\n--- Bibliothek ---")
buch1 = Buch("Der kleine Prinz", "Antoine de Saint-Exupéry")
buch2 = Buch("Harry Potter", "J. K. Rowling")

# Status anzeigen
buch1.status()
buch2.status()


# Buch ausleihen
buch1.ausleihen()
buch1.status()

# Erneut ausleihen
buch1.ausleihen()

# Buch zurückgeben
buch1.zurueckgeben()
buch1.status()

# Noch einmal zurückgeben
buch1.zurueckgeben()