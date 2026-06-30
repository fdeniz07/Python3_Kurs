#---------------------------------------------
# Dateiname: reader.py
# Messdaten aus einem json-File lesen.
#---------------------------------------------



import json, time
DATEINAME = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\messungen\\messdaten.json"                    

try:
    with open(DATEINAME) as stream:
        messungen = json.load(stream)             #1   
except:
    print('Datei konnte nicht geöffnet werden')   #2                                      #3

for datum, messwert in messungen:                 #3
    print(datum, 'Temperatur: ', messwert, '°C')

