#a)
print('\na.Lösung')

liste = [1,2,3,4,5] # Eine Zahlenliste definiert
summe = 0 # Anfang Werte von summe ist 0
for item in liste: # Es gibt hier eine for-Schleife
    summe+=item # Alle items von der Liste addiert in summe-Variable

    durchschnitt = summe / len(liste) # Berechnet durchsnitt von Summe
    print('durchschnittliche Summe :',durchschnitt) # Das ist ein Output. Zeigt durchschnittliche Summe


    #b)
    print('\nb.Lösung')
    zeichenkette = {'a',1,2,4.5,'text'} # in der Zeichenkett gibt es Variables von verschiedene Datentype
    for elements in zeichenkette: # for-Schleife läuft
        print('\n',type(elements)) # zeigen alle typen von der Zeichenkette

    #c)
    print('\nc.Lösung')
    s1= int(input('Geben Sie bitte ein Ganzenzahl ein :'))
    s2= int(input('Geben Sie bitte ein Ganzenzahl ein :'))

    ergebnis = s1 * s2

print(ergebnis)

#d)
print('\nd.Lösung')
print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = int(input("Bitte gib eine Zahl ein: "))
zahl2 = int(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)
