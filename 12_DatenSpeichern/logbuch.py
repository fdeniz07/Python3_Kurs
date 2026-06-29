#---------------------------------------------
# Dateiname: logbuch.py
# Das digitale Logbuch erlaubt das Schreiben von Einträgen
# und das Lesen des gesamten Logbuchs.
#---------------------------------------------
# logbuch.py

from time import asctime

PFAD = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\log.txt"

MENUE = '''
n: Neuer Eintrag
l: Logbuch lesen
e: Ende
'''

def eintragen():
    with open(PFAD, 'a')as logbuch:
        eintrag = asctime() + " "
        eintrag += input('Neuer Eintrag: ')
        logbuch.write(eintrag + '\n')


def lesen ():
    with open(PFAD, 'r') as logbuch:
        text = logbuch.read()
    print(text)
    
    
# Hauptpogramm
auswahl = 'x'    

while auswahl != 'e':
    print(MENUE)
    auswahl = input('Auswahl: ')
    if auswahl == 'n':
        eintragen()
    elif auswahl == 'l':
        lesen()
print('Auf Wiedersehen!')
input()
        

    
                             
