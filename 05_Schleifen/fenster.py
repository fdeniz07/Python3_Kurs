print('Fensterfläche berechnen')
gesamtefläche = 0 
eingabe  = 'j'

while (eingabe == 'j'):

    breite = float(input('Breite des Fensters?(m) : '))
    höhe = float(input('Höhe des Fensters?(m) : '))
    anzahl = int(input('Anzahl der Fenster dieser Größe : '))
    gesamtefläche += breite * höhe * anzahl
    print('Gesamtfläche : ', round(gesamtfläche, 2), 'm2')

    eingabe = input('Weitere Fenster? (j/n): ')
    
print('Auf Wiedersehen!')   
input("\nProgramm beendet. Enter drücken...")
    
