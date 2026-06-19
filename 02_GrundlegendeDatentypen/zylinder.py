# Eingabe
print('Berechnung des Volumens eines Zylinders')
eingabe_h = input('Höhe in Meter: ')
eingabe_d = input('Durchmesser in Meter:') 

# Verarbeitung
h = float(eingabe_h)
d = float(eingabe_d)
volumen = (d/2)**2 * 3.14 * h

# Ausgabe
text = 'Das Volumen beträgt '+ str(volumen) + ' Kubikmeter.'
print(text)
input("Enter drücken...")