#---------------------------------------------
# Dateiname: wortschatz.py
# Das Programm ermittelt, wie viele unterschiedliche
# Wörter in Goethes Faust vorkommen.
#---------------------------------------------
'''
Das Programm arbeitet nach folgendem Verahren:
• Mit der Methode lower() wird dafür gesorgt, dass alle Wörter
kleingeschrieben werden. Sonst würden z.B. »der« und »Der« (am Anfang
eines Satzes) als zwei unterschiedliche Wörter gezählt.
• Mit replace() werden alle Satzzeichen entfernt. Sonst würden z.B. »laufen«
und »laufen« (am Ende eines Satzes) als zwei unterschiedliche Wörter
gezählt.
• Mit split() wird eine Liste von Wörtern gebildet.
• Mit set() wird aus der Liste eine Menge gebildet.
'''

PFAD = 'faust.txt'

file = open(PFAD, mode='r', encoding='utf-8')
text = file.read()
file.close()

print(text[:500]) # Erste 500 Zeichen ausgeben

text = text.lower() # Alle Buchstaben in Kleinbuchstaben umwandeln
for p in '.,:-?!;()_/[]':
     text = text.replace(p, ' ') # Alle Satzzeichen durch Leerzeichen ersetzen. Weil sonst z.B. »laufen« und »laufen« (am Ende eines Satzes) als zwei unterschiedliche Wörter gezählt würden.
wortliste = text.split() # Die Methode split() teilt den Text in einzelne Wörter auf und speichert sie in einer Liste.
wortmenge = set(wortliste) # Die Methode set() wandelt die Liste in eine Menge um. In einer Menge gibt es keine doppelten Elemente, daher werden alle mehrfach vorkommenden Wörter automatisch entfernt.

print('\nWörter insgesamt:', len(wortliste))
print('\nUnterschiedliche Wörter:', len(wortmenge))
print('\n',list(wortmenge)[:50],'\n')


