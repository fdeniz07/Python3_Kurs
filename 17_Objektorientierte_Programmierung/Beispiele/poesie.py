# ---------------------------------------------------
# Dateiname: poesie.py
# Verwaltung einer Sammlung von Sprüchen
#----------------------------------------------------

class Spruch:
  'Die Klasse modelliert einen Spruch'
  def __init__(self, text, anlass):
    self.text = text
    self.anlass = anlass

class Sammlung:
  'Modeliert eine Sammlung von Sprüchen'
  def __init__(self):
    self.sprüche = []

  def neu(self, text, anlass):
    texte = [spruch.text for spruch in self.sprüche]
    if text not in texte:
        neu = Spruch(text, anlass)
        self.sprüche.append(neu)

  def suche(self, anlass):
    'Liefert einen Text mit Sprüchen zum gegebenen Anlass.'
    ausgabe = ''
    for spruch in self.sprüche:
        if anlass == spruch.anlass:
            ausgabe += spruch.text + '\n'
    return ausgabe

  def suche_anlässe(self):
    'Liefert Menge mit allen Anlässen der Sammlung.'
    return {spruch.anlass for spruch in self.sprüche}

  def __str__(self):
    ausgabe = ''
    for spruch in self.sprüche:
        ausgabe += spruch.text + '\n'
    return ausgabe 

if __name__ == '__main__':
    album = Sammlung()
    album.neu('Morgenstund hat Gold im Mund.',
              'Frühstück')
    album.neu('Der frühe Vogel fängt den Wurm.',
              'Frühstück')
    album.neu('Wer A sagt muss auch B sagen.',
              'Hochzeit')

    print(album.suche_anlässe())
    print(album.suche('Frühstück'))
    
   

