#---------------------------------------------
# Dateiname: writer.py
# Messdaten eingeben und in json-File schreiben.
#---------------------------------------------
import json, time
DATEINAME = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\messungen\\messdaten.json"                    #1

try:
    with open(DATEINAME) as stream:             #2
        messungen = json.load(stream)           #3
except:
    messungen = []                              #4
print('Zum Beenden der Eingabe ENTER drücken.')
eingabe = input('Temperatur in C: ')
while eingabe:
    eintrag = [time.asctime(), 
               round(float(eingabe), 3)]        #5
    messungen.append(eintrag)                   #6
    eingabe = input('Temperatur in C: ')

with open(DATEINAME, 'w') as stream:
    json.dump(messungen, stream)                #7

