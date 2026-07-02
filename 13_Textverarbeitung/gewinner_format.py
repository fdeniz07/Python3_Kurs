#---------------------------------------------
# Dateiname: gewinner.py
# Das Programm ermittelt einen Gewinner und
# schreibt eine Mitteilung.
#---------------------------------------------
# gewinner.py
from random import choice
PERSONEN = ['Tina', 'Anna', 'Kim', 'Niels']
SCHABLONE = 'Der Gewinner ist {}.'
gewinner = choice(PERSONEN)
print(SCHABLONE.format(gewinner))

