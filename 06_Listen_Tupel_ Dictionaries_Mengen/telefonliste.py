# telefon.py

# Liste von Tupeln für die Telefonbucheinträge
TEL = [
    ('Lukas', '030 8472911'),
    ('Emma', '089 5534120'),
    ('Maximilian', '040 3195844'),
    ('Mia', '069 4620199'),
    ('Jonas', '0221 7843110'),
    ('Hannah', '0711 6352488'),
    ('Leon', '0211 9154322'),
    ('Sofia', '0421 2786533'),
    ('Finn', '0341 4958100'),
    ('Anna', '0231 5634211')
]

# Menü-Text exakt wie in der Ausgabe vorgegeben
MENÜ = '''(T)elefonnummer suchen
(N)ame suchen
(E)nde'''

# Funktion sucht die Telefonnummer anhand des Namens (Muss mit dem Suchwort BEGINNEN)
def suche_nummern(suchwort):
    gefundene_treffer = False
    for name, nummer in TEL:
        # Prüft, ob der Name mit dem eingegebenen Suchwort beginnt (Groß-/Kleinschreibung ignoriert)
        if name.lower().startswith(suchwort.lower()):
            print(name, nummer)
            gefundene_treffer = True
            
    # Wenn kein Eintrag mit diesem Namen beginnt
    if not gefundene_treffer: not_found()

# Funktion sucht den Namen anhand der Telefonnummer (Muss mit den Ziffern BEGINNEN)
def suche_namen(ziffern):
    gefundene_treffer = False
    for name, nummer in TEL:
        # Leerzeichen entfernen, um eine sauberere Prüfung am Anfang zu ermöglichen
        formatierte_nummer = nummer.replace(" ", "")
        
        # Prüft, ob die Nummer mit den Ziffern beginnt
        if nummer.startswith(ziffern) or formatierte_nummer.startswith(ziffern):
            print(name, nummer)
            gefundene_treffer = True
            
    # Wenn kein Eintrag mit diesen Ziffern beginnt
    if not gefundene_treffer: not_found()


def not_found():
    print("Keine Einträge gefunden.")   


# Erster Durchlauf des Menüs
print(MENÜ)
eingabe = input('Auswahl (t, n, e): ').strip().lower()

# Hauptschleife für die Menüsteuerung
while eingabe != 'e':
    # Wenn die Eingabe ungültig ist, wird der Benutzer darauf hingewiesen
    if eingabe not in ['t', 'n', 'e']:
        print("Ungültige Eingabe! Bitte wählen Sie nur 't', 'n' oder 'e'.")
    
    # Wenn die Eingabe 'n' ist, wird nach Namen gesucht (Suchwort)
    elif eingabe == 'n':
        suchwort = input('Suchwort: ')
        suche_nummern(suchwort)
        
    # Wenn die Eingabe 't' ist, wird nach Nummern gesucht (Ziffern)
    elif eingabe == 't':
        ziffern = input('Ziffern: ')
        suche_namen(ziffern)
        
    # Menü erneut anzeigen und nächste Eingabe holen
    print('\n' + MENÜ)
    eingabe = input('Auswahl (t, n, e): ').strip().lower()

print('Bis bald!')