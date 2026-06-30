# a) Initiale Liste
einkaufsliste = ["Äpfel", "Brot", "Milch", "Eier", "Käse"]

# b)
def einkauf_hinzufuegen(lebensmittel):
    """Fügt ein Lebensmittel hinzu, wenn es noch nicht existiert."""
    if lebensmittel in einkaufsliste:
        print(f"'{lebensmittel}' ist bereits in der Liste!")
    else:
        einkaufsliste.append(lebensmittel)
        print(f"'{lebensmittel}' zur Einkaufsliste hinzugefügt.")

DATEI_PFAD = r"c:\\PROJEKTE_LOKAL\\BILDUNGS\\VelpTEC\\Python3_Kurs\\12_DatenSpeichern\\einkaufliste\\einkaufsliste.txt"



# c) Benutzereingaben (bis zu 3 Mal)
for i in range(3):
     neues_lebensmittel = input("Füge ein neues Lebensmittel hinzu: ")
     einkauf_hinzufuegen(neues_lebensmittel)

# d) & e) Speichern in Datei mit Fehlerbehandlung
try:
    with open(DATEI_PFAD, "w", encoding="utf-8") as datei:
        for item in einkaufsliste:
            datei.write(f"{item}\n")
    print("\nEinkaufsliste wurde erfolgreich in 'einkaufsliste.txt' gespeichert.")
except IOError as e:
    print(f"Fehler beim Schreiben der Datei: {e}")

# f) Lesen und Ausgabe aus der Datei mit Fehlerbehandlung
print("\nAktueller Inhalt der 'einkaufsliste.txt':")
try:
    with open(DATEI_PFAD, "r", encoding="utf-8") as datei:
        for zeile in datei:
            print(f"- {zeile.strip()}")
except FileNotFoundError:
    print("Fehler: Die Datei 'einkaufsliste.txt' wurde nicht gefunden.")
except IOError as e:
    print(f"Fehler beim Lesen der Datei: {e}")