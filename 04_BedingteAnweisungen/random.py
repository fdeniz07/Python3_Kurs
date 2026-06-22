'''
Frage 1: Berechnung der Anzahl der Ziffern
Beschreibung:
Berechnen Sie, aus wie vielen Ziffern eine von Ihnen generierte Zufallszahl (maximal 5-stellig) besteht.

Frage 2: Warenkorb- und Preisberechnung
Beschreibung:
Stellen Sie sich vor, Sie schreiben ein Programm zur Preisberechnung. Aktualisieren Sie den Gesamtpreis basierend darauf, ob der Benutzer eine Ratenzahlung wünscht und ob er eine Kundenkarte besitzt.
Bedingung 1 -> Wenn Ratenzahlung gewünscht wird: Bei 3 Raten gibt es einen Preisaufschlag von 3 %, bei 6 Raten 6 % und bei 9 Raten 9 %.
Bedingung 2 -> Wenn eine Kundenkarte vorhanden ist, wird ein Rabatt von 10 % gewährt.

Frage 3: Berechnung der Dreiecksbildung-Bedingung
Beschreibung:
Fragen Sie den Benutzer nach den drei Seitenlängen eines Dreiecks (x, y, z) und überprüfen Sie anschließend anhand dieser Werte, ob ein gültiges Dreieck gebildet werden kann.
Bedingung 1 -> Für die Seite x: |y - z| < x < y + z muss gelten.
Bedingung 2 -> Für die Seite y: |x - z| < y < x + z muss gelten.
Bedingung 3 -> Für die Seite z: |x - y| < z < x + y muss gelten.
'''

import random

# Lösung für Frage 1:
zufallszahl = random.randint(1, 99999)

if zufallszahl < 10:
    print("Die Zahl {} besteht aus einer Ziffer.".format(zufallszahl))
elif zufallszahl < 100:
    print("Die Zahl {} besteht aus zwei Ziffern.".format(zufallszahl))
elif zufallszahl < 1000:
    print("Die Zahl {} besteht aus drei Ziffern.".format(zufallszahl))
elif zufallszahl < 10000:
    print("Die Zahl {} besteht aus vier Ziffern.".format(zufallszahl))
else:
    print("Die Zahl {} besteht aus fünf Ziffern.".format(zufallszahl))