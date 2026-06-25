# vokabeltrainer.py
from random import choice

def aufgabe(d):
    # #1: Funktion definiert den kompletten Dialog bei einer Aufgabe
    # #2: Aus der Liste der englischen Wörter (Schlüssel) wird ein Wort zufällig ausgewählt
    vokabel = choice(list(d.keys()))
    
    # #3: Die Aufgabe wird gestellt
    print('Nennen Sie ein deutsches Wort für', vokabel + '!')
    antwort = input('Deutsches Wort: ')
    
    # #4: Prüfen, ob die Antwort in der Liste der deutschen Wörter vorkommt
    if antwort not in d[vokabel]:
        print('Leider falsch.')
        # #5: end=' ' bewirkt, dass kein Zeilenumbruch erfolgt
        print(vokabel, 'bedeutet:', end=' ')
        # #6: Alle richtigen Wörter hintereinander in der gleichen Zeile ausgeben
        for wort in d[vokabel]:
            print(wort, end=' ')
        # #7: Erzeugt den abschließenden Zeilenumbruch
        print()
    else:
        # #8: Falls richtig, wird das Item aus dem Dictionary gelöscht
        print('Richtig!')
        del d[vokabel]

# Hauptprogramm
# #9: Definition des Wörterbuchs mit Listen als Werten
d = {'sun': ['Sonne'],
     'key': ['Taste', 'Schlüssel'],
     'head': ['Kopf', 'Chef', 'Leiter']}

# #10: Solange das Dictionary d nicht leer ist (Wahrheitswert True)
while d:
    aufgabe(d)

# #11: Erst wenn das Dictionary leer ist, geht es hier weiter
print('Sie haben alle Vokabeln gelernt.')

# #12: Wartet auf das Drücken der Enter-Taste vor dem Beenden
eingabe = input()