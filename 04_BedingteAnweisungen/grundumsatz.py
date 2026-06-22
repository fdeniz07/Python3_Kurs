print("Grundumsatz-Anwendung")
m=float(input('Bitte geben Sie Ihres Körpergewicht in kg ein : '))
h=float(input('Bitte geben Sie Ihre Körpergröße in cm ein : '))
a=float(input('Bitte geben Sie Ihres Alter in Jahren ein : '))
g=input('Bitte geben Sie Ihres Geschlecht in M oder F ein : ')
grund_Umsatz = 0

if(g=='M') or (g=='m'):
    grund_Umsatz = 66.5 + (13*m) + (5*h) - (6.8*a)
elif (g=='F') or (g=='f'):
    grund_Umsatz = 65.5 + (9.6*m) + (1.8*h) - (4.7*a)
else:
    print('Bitte geben Sie richtige Antwort ein!')


print('Ihren Grundumsatz beträgt :', grund_Umsatz, 'kcal pro Tag.. Diese Energie braucht Ihr Körper im Ruhezustand.')
input("\nProgramm beendet. Enter drücken...")

