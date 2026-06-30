#---------------------------------------------
# Dateiname: platzbedarf.py
# Ausgegeben wird die Anzahl aller Verzeichnisse
# und der Speicherplatzbedarf aller Dateien in
# einem Verzeichnisbaum.
#---------------------------------------------
import os                                               

BERICHT =  '''
Ich habe {} Verzeichnisse durchsucht.
Der gesamte Speicherbedarf beträgt {} Bytes.'''        #1                                           #1

def berechne_platzbedarf(wurzel):                    
    durchlauf = os.walk(wurzel)                        #2
    anzahl = 0
    platz = 0
    for v, uv, d in durchlauf:                         #3
        anzahl += 1                                    #4
        os.chdir(v)                                    #5
        for datei in d:  
            platz += os.path.getsize(datei)            #6        
    return anzahl, platz                               #7
    
wurzel = input('Wurzelverzeichnis (z.B. /python310): ')
if os.path.exists(wurzel):                             #8
    anz_verz, speicher = berechne_platzbedarf(wurzel)  #9
    print(BERICHT.format(anz_verz, speicher))
else:
    print('Ungültiger Pfad')
input()