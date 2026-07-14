class Auto:
    def __init__(self, marke, modell, kilometerstand, tankfüllung):
        self.marke = marke
        self.modell = modell
        self.kilometerstand = kilometerstand
        self.tankfüllung = tankfüllung


    def fahren(self, kilometer):
        self.kilometerstand += kilometer
        verbrauch = (kilometer / 100) * 5
        self.tankfüllung -= verbrauch
        if self.tankfüllung < 0:
            self.tankfüllung = 0
        print(f"Gefahrene Kilometer: {kilometer}. Verbleibende Tankfüllung: {self.tankfüllung}%.")


    def tanken(self, prozent):
        if self.tankfüllung + prozent > 100:
            self.tankfüllung = 100
        else:
            self.tankfüllung += prozent
        print(f"Getankte Menge: {prozent}%. Neue Tankfüllung: {self.tankfüllung}%.")


# Beispiel zur Nutzung der Klasse

mein_auto = Auto("Volkswagen", "Golf", 50000, 50)
mein_auto.fahren(200)
mein_auto.tanken(20)