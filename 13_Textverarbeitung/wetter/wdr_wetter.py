#---------------------------------------------
# Dateiname: wdr_wetter.py
# Das Programm analysiert die Webseite des WDR
# und extrahiert eine Wetterprognose.
#---------------------------------------------
from urllib.request import urlopen

URL = "https://www1.wdr.de/index.html"

f = urlopen(URL)

htmltext = f.read().decode("utf-8")

f.close()

liste = htmltext.split("Heute bis")

if len(liste) > 1:
    temperatur = liste[1].split("Grad")[0].strip()

    print("Wie warm wird es heute?")
    print("Höchsttemperatur:", temperatur + "°C")
else:
    print("Temperatur nicht gefunden.")
