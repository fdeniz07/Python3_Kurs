class Student:
    def __init__(self, vorname, nachname, fachbereich):
        self.vorname = vorname
        self.nachname = nachname
        self.fachbereich = fachbereich
        print("Student wurde erstellt")

    def zeige_infos(self):
        print("Vorname:", self.vorname)
        print("Nachname:", self.nachname)
        print("Fachbereich:", self.fachbereich)
