
def temperatur_umrechner(temperatur:float,einheit='C'):
    if einheit == 'F':
       return(temperatur-32)*5/9
    elif einheit == 'C':
       return temperatur*9/5 + 32
    else:
        return None


while True:

    einheit = input('Celsius(C) oder Fahrenheit(F): ').upper()
        
    
    if einheit == 'F':
        einheit_werte = 'Fahrenheit'
    elif einheit == 'C':
         einheit_werte = 'Celsius'
    else:
        print('Bitte gib eine gültige Einheit ("C" oder "F") ein.')
   

    if einheit == 'F' or einheit == 'C':
        temperatur = float(input('Temperatur: ' ))
        
        if einheit:
            t = temperatur_umrechner(temperatur, einheit)
            wert = 'Celsius'
            print(temperatur, einheit_werte, 'entspricht',float(round(t,2)), wert)
            input("\nProgramm beendet. Enter drücken...")
        else:
            t = temperatur_umrechner(temperatur)
            wert = 'Fahrenheit'
            print(temperatur, einheit_werte,'entspricht',float(round(t,2)), wert)
            input("\nProgramm beendet. Enter drücken...")

    
input("\nProgramm beendet. Enter drücken...")

