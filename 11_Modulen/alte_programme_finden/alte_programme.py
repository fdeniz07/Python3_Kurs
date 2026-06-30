#---------------------------------------------
# Dateiname: alte_programme.py
# Alte Dateien finden
#---------------------------------------------
import os,time                                               

def finde_alte_programme(p):
    '''Argument p ist ein gültiger Pfad eines Verzeichnisses.
       Die Funktion liefert Liste
       mit 2-Tupeln der Form (datei, alter)
       Mit Name und Alter von Python-Programmdateien
       in Ordner p, die älter als 30 Tage sind'''

    alte_programme = []                                 #1                           
    os.chdir(p)                                         #2                                   
    for name in os.listdir():                          #3
        alter_s = time.time() - os.path.getmtime(name) #4
        alter = alter_s / (24 * 3600)                   #5          
        if name.endswith('.py') and (alter > 2):      #6                
           alte_programme.append((name, alter))
    return alte_programme                               #7
                                     
# Hauptprogramm   
pfad = input('Verzeichnis: ')                        
if os.path.isdir(pfad):
    alt = finde_alte_programme(pfad)                    #8
    for programm, alter in alt:                  
         print(programm, round(alter), 'Tage alt')                                
    print(len(alt), 'Dateien gefunden')                 #9
else:
    print('Ungültiger Pfad')
input()

