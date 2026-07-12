'''
Aufgabe: Objektorientierte Programmierung
Entwickle eine Python-Klasse Auto, die verschiedene Attribute wie marke, modell, baujahr und kilometerstand hat. 
Die Klasse sollte folgende Methoden beinhalten: 

a) Eine Initialisierungsmethode, die es ermöglicht, bei der Erstellung eines Auto-Objekts die Marke, 
das Modell und das Baujahr anzugeben, während der Kilometerstand standardmäßig auf 0 gesetzt wird. 

b) Eine Methode fahren, die den Kilometerstand um die gefahrenen Kilometer erhöht, die als Parameter übergeben werden. 

c) Eine Methode anzeigen, die die Details des Autos (Marke, Modell, Baujahr, Kilometerstand) in einer lesbaren Form ausgibt.

Stelle sicher, dass du die Konzepte der objektorientierten Programmierung korrekt anwendest, 
insbesondere die Definition von Klassen, die Initialisierung von Objekten und das Aufrufen von Methoden. Teste deine Klasse, indem du mindestens zwei Auto-Objekte erstellst, mit der Methode fahren den Kilometerstand änderst und schließlich die Details jedes Autos mit der Methode anzeigen ausgibst. 
'''



class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0

    def fahren(self, kilometer):
        self.kilometerstand += kilometer

    def anzeigen(self):
        print("----- Auto -----")
        print(f"Marke: {self.marke}")
        print(f"Modell: {self.modell}")
        print(f"Baujahr: {self.baujahr}")
        print(f"Kilometerstand: {self.kilometerstand} km")
        print()


# Zwei Auto-Objekte erstellen
auto1 = Auto("BMW", "3er", 2020)
auto2 = Auto("Audi", "A4", 2018)

# Mit den Autos fahren
auto1.fahren(150)
auto1.fahren(75)

auto2.fahren(320)

# Informationen anzeigen
auto1.anzeigen()
auto2.anzeigen()