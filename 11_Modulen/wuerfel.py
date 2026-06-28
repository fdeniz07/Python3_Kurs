# Aufgabe: Module
# Wuerfel-Programm mit Zeitstempel

# a) Module importieren
import random
import time


# b) Funktion wuerfeln()
# Diese Funktion gibt eine zufaellige Zahl zwischen 1 und 6 zurueck
def wuerfeln():
    zahl = random.randint(1, 6)
    return zahl


# c) Funktion aktueller_timestamp()
# Diese Funktion gibt den aktuellen Unix-Timestamp zurueck
def aktueller_timestamp():
    timestamp = time.time()
    return timestamp


# d) und e) Hauptschleife mit 5 Durchlaeufen und Pause
for i in range(1, 6):
    wurf = wuerfeln()
    timestamp = aktueller_timestamp()

    print(f"Wurf {i}: {wurf} | Timestamp: {timestamp}")

    # e) Pause von 2 Sekunden zwischen den Wuerfen
    # sleep() haelt das Programm fuer die angegebene Anzahl von Sekunden an
    if i < 5:
        time.sleep(2)
