#---------------------------------------------
# Dateiname: bremsweg.py
# Das Programm fragt Geschwindigkeit und  
# Bremsverzögerung und berechnet den Bremsweg.
# Autor: Fatih Deniz
# Python für Studium und Ausbildung
#---------------------------------------------
# Eingabe
print('Bremsweg eines Autos')                                
v_kmh = float(input('Geschwindigkeit in km/h: '))           
print('Geben Sie die Bremsverzögerung an!')
print('(Nass: 7, trocken: 8)')
a = float(input('Bremsverzögerung: '))  

# Verarbeitung
v = v_kmh / 3.6   # Umrechnung der Geschwindigkeit in m/s
s = v**2 / (2 * a)                                     

# Ausgabe
print('Der Bremsweg beträgt', round(s), 'Meter.')            
input("Enter drücken...")