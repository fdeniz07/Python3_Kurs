'''
Aufgabe: Objektorientierte Programmierung
Erstelle eine Klasse Auto, welche folgende Attribute besitzt: marke (String), modell (String), 
kilometerstand (Integer) und tankfüllung (in Prozent als Integer). Die Klasse soll zwei Methoden haben: 
fahren(kilometer) und tanken(prozent). Die Methode fahren(kilometer) soll den Kilometerstand um die gefahrenen 
Kilometer erhöhen und die Tankfüllung basierend auf einer Annahme, dass das Auto pro 100 Kilometer 
5% des Tanks verbraucht, reduzieren. Die Methode tanken(prozent) soll die Tankfüllung um den angegebenen Prozentsatz 
erhöhen, darf aber 100% nicht überschreiten.
'''

"""Einfache Auto-Klasse fuer eine OOP-Uebung."""


class Auto:
	"""Repraesentiert ein Auto mit Kilometerstand und Tankfuellung in Prozent."""

	def __init__(self, marke, modell, kilometerstand, tankfuellung):
		if kilometerstand < 0:
			raise ValueError("Der Kilometerstand darf nicht negativ sein.")
		if not 0 <= tankfuellung <= 100:
			raise ValueError("Die Tankfuellung muss zwischen 0 und 100 liegen.")

		self.marke = marke
		self.modell = modell
		self.kilometerstand = int(kilometerstand)
		self.tankfuellung = int(tankfuellung)

	def fahren(self, kilometer):
		"""Erhoeht den Kilometerstand und reduziert die Tankfuellung.

		Annahme: Pro 100 Kilometer werden 5 Prozentpunkte Tank verbraucht.
		"""
		if kilometer < 0:
			raise ValueError("Gefahrene Kilometer duerfen nicht negativ sein.")

		self.kilometerstand += int(kilometer)
		verbrauch = kilometer * 5 / 100
		self.tankfuellung = max(0, int(round(self.tankfuellung - verbrauch)))

	def tanken(self, prozent):
		"""Erhoeht die Tankfuellung um den angegebenen Prozentwert bis maximal 100."""
		if prozent < 0:
			raise ValueError("Der Tankbetrag darf nicht negativ sein.")

		self.tankfuellung = min(100, self.tankfuellung + int(prozent))

	def __str__(self):
		return (
			f"{self.marke} {self.modell} | "
			f"Kilometerstand: {self.kilometerstand} km | "
			f"Tank: {self.tankfuellung}%"
		)


def main():
	auto = Auto("Volkswagen", "Golf", 12500, 70)
	print("Start:", auto)

	auto.fahren(150)
	print("Nach 150 km:", auto)

	auto.tanken(40)
	print("Nach dem Tanken:", auto)


if __name__ == "__main__":
	main()
