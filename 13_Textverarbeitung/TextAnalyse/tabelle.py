#---------------------------------------------
# Dateiname: tabelle.py
# Das Programm analysiert einen Text
# und erstellt eine Tabelle mit den am
# häufigsten vorkommenden Wörtern mit
# mehr als 5 Buchstaben.
#---------------------------------------------
                      #1

import json
import os

ZEILE = '{:15}|{:10}'       

# Pfad-Konfiguration für die Datei
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def häufigste_wörter(text, minlänge, anzahl):
    for ch in '${}<>.,;:/?!"-_[]':                #2
        text = text.replace(ch, ' ')
    wortliste = text.split()                      #3
    wortmenge = set(wortliste)                    #4
    häufigkeiten = [(text.count(wort), wort)
                    for wort in wortmenge
                    if len(wort) >= minlänge]     #5
    häufigkeiten.sort()                           #6
    häufigkeiten.reverse()                        #7
    return häufigkeiten[0:anzahl]                 #8
    
def ausgabe(häufigkeiten):
    print(ZEILE.format('Wort', ' Vorkommen'))
    print(26*'-')                                 #9       
    for vorkommen, wort in häufigkeiten:
        print(ZEILE.format(wort, vorkommen))
          
# Hauptprogramm
dateiname = input('Dateiname: ')
minlänge = int(input('Minimale Wortlänge: '))        
anzahl = int(input('Länge der Tabelle: '))


DATEI_NAME = os.path.join(BASE_DIR, dateiname)

f = open(DATEI_NAME, 'r', encoding='utf-8')        #10
text=f.read()
f.close
tabelle = häufigste_wörter(text, minlänge, anzahl)
ausgabe(tabelle)               
input()


'''
## Ausgabe

```text
Dateiname: faust.txt
Minimale Wortlänge: 6
Länge der Tabelle: 5
```

| Wort           | Vorkommen |
| :------------- | --------: |
| Mephisto       |       287 |
| Mephistopheles |       286 |
| Margarete      |        86 |
| gleich         |        68 |
| Mensch         |        55 |

'''