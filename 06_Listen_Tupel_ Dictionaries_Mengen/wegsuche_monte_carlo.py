#---------------------------------------------
# Suche eines Weges in einem Graphen nach
# einem Monte-Carlo-Algorithmus
#---------------------------------------------
from random import choice
G = {1: [2, 4], 2: [1, 3, 5], 3: [2, 5],
     4: [1, 5], 5: [4, 2, 3, 6], 6: [5]}

def suche_weg(aktuell, ziel):
    if ziel == aktuell:
        return [aktuell]
    else:
        while not ziel in weg:
           weg = suche_weg(choice(G[aktuell]), ziel)
        return [aktuell] + weg


while True:
    start = int(input('Start: '))
    ziel = int(input('Ziel: '))
    weg = suche_weg(start, ziel)
    print('Weg:', weg)


