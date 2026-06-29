#---------------------------------------------
# Dateiname: newscheck.py
# Das Programm prüft, ob ein betimmtes Stichwort 
# auf einer Webseite vorkommt.
#---------------------------------------------


from urllib.request import urlopen

URL = 'https://www1.wdr.de/index.html'


def kommt_vor(stichwort:str)-> bool:
    'Prüft, ob ein Stichwort auf einer Webseite vorkommt.'
    webseite = urlopen(URL)
    rohdaten = webseite.read()
    webseite.close()
    text = rohdaten.decode()
    return stichwort in text
        
# Hauptpogramm
stichwort = input('Stichwort: ')     
while stichwort:
    if kommt_vor(stichwort):
        print('"' + stichwort +'"',
              'kommt auf der Startseite des WDR vor.')
    else:
        print('"' + stichwort +'"',
              'wird auf der Startseite des WDR nicht erwähnt.')
    stichwort = input('Stichwort: ')
print('Auf Wiedersehen!')
input()
        

    
                             
