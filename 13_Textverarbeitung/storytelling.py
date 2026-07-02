#---------------------------------------------
# Dateiname: storytelling.py
# Das Programm fragt nach einigen Wörtern und
# erzählt dann eine Geschichte, in der die Wörter
# vorkommen.
#---------------------------------------------
from random import choice
STORY = '''Am Morgen ging {sie} mit ihrem {gegenstand} über 
den Prinzipalmarkt. "Ach", dachte {sie}, "wie gut,
dass ich den {gegenstand} dabei habe. Ohne {gegenstand} käme
ich mir irgendwie unvollständig vor." '''
ORTE = ['Prinzipalmarkt', 'Domplatz']
sie = input("Weiblicher Vorname: ")
gegenstand = input("Gegenstand (männlich): ")
story = STORY.format(sie=sie,
                     gegenstand=gegenstand,
                     ort=choice(ORTE))
print(story)

