# Eingabe
print('Berechnung des Volumens eines Zylinders')
eingabe_h = input('Höhe in Meter: ')
eingabe_d = input('Durchmesser in Meter:') 

try:
    h = float(eingabe_h)
    d = float(eingabe_d)
    volumen = (d/2)**2 * 3.14 * h

    text = 'Das Volumen beträgt ' + str(volumen) + ' Kubikmeter.'
    print(text)

except Exception as e:
    print("Fehler:", e)

input("Enter drücken...")