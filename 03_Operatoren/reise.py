#---------------------------------------------
# Dateiname: reise.py
# Das Programm berechnet die Kosten für eine
# Gruppenreise.
# Autor: Fatih Deniz
#---------------------------------------------

# Eingabe
print('Kostenplan für eine Reise')
print('-------------------------')
bus = float(input('Kosten für den Reisebus (€): '))      #1
hotel = float(input('Hotelkosten pro Person (€): '))
reiseführer = float(input('Reiseführer(€): '))
personenzahl = int(input('Anzahl der Teilnehmer*innen: '))

# Verarbeitung
gesamtkosten = bus + reiseführer + personenzahl * hotel 
kosten_pro_person = gesamtkosten / personenzahl

# Ausgabe
print('Gesamtkosten: ', gesamtkosten, '€')               #2
print('Kosten pro Person: ', kosten_pro_person, '€')
input("\nProgramm beendet. Enter drücken...")