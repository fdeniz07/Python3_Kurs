def temperatur_umrechner(temperatur, einheit='C'):
    if einheit == 'C':
        return temperatur * 9/5 + 32
    elif einheit == 'F':
        return (temperatur - 32) * 5/9
    else:
        return None
while True:
    eingabe = input("Gib eine Temperatur mit Einheit ein (z.B. '35 C' oder '95 F'), oder 'ende' zum Beenden: ")
    if eingabe.lower() == 'ende':
        break
    try:
        teile = eingabe.split()
        temp = float(teile[0])
        if len(teile) == 2:
            einheit = teile[1].upper()
        else:
            einheit = 'C'  # Standardwert, wenn keine Einheit angegeben ist
        umgerechnet = temperatur_umrechner(temp, einheit)
        if umgerechnet is not None:
            if einheit == 'C':
                print(f"{temp} °C entspricht {umgerechnet} °F")
            else:
                print(f"{temp} °F entspricht {umgerechnet} °C")
        else:
            print("Bitte gib eine gültige Einheit ('C' oder 'F') ein.")
    except ValueError:
        print("Bitte gib eine gültige Zahl für die Temperatur ein.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
