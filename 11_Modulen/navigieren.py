#---------------------------------------------
# Dateiname: navigieren
# Interaktives Programm, das durch den Verzeichnisbaum navigiert und
# jeweils den Namen und den Inhalt des aktuellen Arbeitsverzeichnis ausgibt
#---------------------------------------------


import os

pfad = os.getcwd() 
while pfad:
    print('Arbeitsverzeichnis: ' + os.getcwd()) #1
    print('Inhalt:')
    for d in os.listdir():                      #2
        print(d)
    pfad = input('Gewünschtes Verzeichnis): ')  #3
    if os.path.exists(pfad):                    #4       
        os.chdir(pfad)             
    elif pfad:                                  #5
        print('Ungültiger Pfad')
print('Auf Wiedersehen!')                       #6
input()                                         #7
