import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Mitarbeiter:
    def __init__(self, name, position, abteilung, gehalt, einstellungsdatum):
        self.name = name
        self.position = position
        self.abteilung = abteilung
        self.gehalt = gehalt
        self.einstellungsdatum = einstellungsdatum
    

    def zeige_daten(self):
        return f"Name: {self.name}, Position: {self.position}, Abteilung: {self.abteilung}, Gehalt: {self.gehalt}, Einstellungsdatum: {self.einstellungsdatum}"


class MitarbeiterVerwaltung:
    def __init__(self):
        self.mitarbeiter_liste = []
    

    def hinzufuegen(self, mitarbeiter):
        self.mitarbeiter_liste.append(mitarbeiter)
    

    def aktualisieren(self, name, neue_daten):
        for mitarbeiter in self.mitarbeiter_liste:
            if mitarbeiter.name == name:
                mitarbeiter.position, mitarbeiter.abteilung, mitarbeiter.gehalt, mitarbeiter.einstellungsdatum = neue_daten
                return True
        return False
    

    def loeschen(self, name):
        for mitarbeiter in self.mitarbeiter_liste:
            if mitarbeiter.name == name:
                self.mitarbeiter_liste.remove(mitarbeiter)
                return True
        return False
    

    def suchen(self, suchbegriff):
        ergebnisse = []
        for mitarbeiter in self.mitarbeiter_liste:
            if suchbegriff.lower() in mitarbeiter.name.lower() or suchbegriff.lower() in mitarbeiter.abteilung.lower():
                ergebnisse.append(mitarbeiter.zeige_daten())
        return ergebnisse


class App:

    def __init__(self, root):
        self.verwaltung = MitarbeiterVerwaltung()
        self.root = root
        self.root.title("Mitarbeiterverwaltung")
        

        # Widgets für die Eingabe von Mitarbeiterdaten
        self.eingabe_frame = ttk.Frame(self.root)
        self.eingabe_frame.grid(row=0, column=0, padx=10, pady=10)
        

        self.name_label = ttk.Label(self.eingabe_frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.eingabe_frame)
        self.name_entry.grid(row=0, column=1)
        

        self.position_label = ttk.Label(self.eingabe_frame, text="Position:")
        self.position_label.grid(row=1, column=0, sticky=tk.W)
        self.position_entry = ttk.Entry(self.eingabe_frame)
        self.position_entry.grid(row=1, column=1)
        

        self.abteilung_label = ttk.Label(self.eingabe_frame, text="Abteilung:")
        self.abteilung_label.grid(row=2, column=0, sticky=tk.W)
        self.abteilung_entry = ttk.Entry(self.eingabe_frame)
        self.abteilung_entry.grid(row=2, column=1)
        

        self.gehalt_label = ttk.Label(self.eingabe_frame, text="Gehalt:")
        self.gehalt_label.grid(row=3, column=0, sticky=tk.W)
        self.gehalt_entry = ttk.Entry(self.eingabe_frame)
        self.gehalt_entry.grid(row=3, column=1)
        

        self.einstellungsdatum_label = ttk.Label(self.eingabe_frame, text="Einstellungsdatum:")
        self.einstellungsdatum_label.grid(row=4, column=0, sticky=tk.W)
        self.einstellungsdatum_entry = ttk.Entry(self.eingabe_frame)
        self.einstellungsdatum_entry.grid(row=4, column=1)
        

        self.hinzufuegen_button = ttk.Button(self.eingabe_frame, text="Hinzufügen", command=self.hinzufuegen)
        self.hinzufuegen_button.grid(row=5, column=0, columnspan=2, pady=5)
        

        self.aktualisieren_button = ttk.Button(self.eingabe_frame, text="Aktualisieren", command=self.aktualisieren)
        self.aktualisieren_button.grid(row=6, column=0, columnspan=2, pady=5)
        

        self.loeschen_button = ttk.Button(self.eingabe_frame, text="Löschen", command=self.loeschen)
        self.loeschen_button.grid(row=7, column=0, columnspan=2, pady=5)
        

        self.suchen_label = ttk.Label(self.eingabe_frame, text="Suchen:")
        self.suchen_label.grid(row=8, column=0, sticky=tk.W)
        self.suchen_entry = ttk.Entry(self.eingabe_frame)
        self.suchen_entry.grid(row=8, column=1)
        self.suchen_button = ttk.Button(self.eingabe_frame, text="Suchen", command=self.suchen)
        self.suchen_button.grid(row=9, column=0, columnspan=2, pady=5)
        

        # Widgets für die Anzeige von Suchergebnissen
        self.ergebnis_frame = ttk.Frame(self.root)
        self.ergebnis_frame.grid(row=1, column=0, padx=10, pady=10)
        

        self.ergebnis_label = ttk.Label(self.ergebnis_frame, text="Ergebnisse:")
        self.ergebnis_label.grid(row=0, column=0, sticky=tk.W)
        self.ergebnis_text = tk.Text(self.ergebnis_frame, height=10, width=50)
        self.ergebnis_text.grid(row=1, column=0)
    

    def hinzufuegen(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        abteilung = self.abteilung_entry.get()
        gehalt = self.gehalt_entry.get()
        einstellungsdatum = self.einstellungsdatum_entry.get()
        

        if name and position and abteilung and gehalt and einstellungsdatum:
            mitarbeiter = Mitarbeiter(name, position, abteilung, gehalt, einstellungsdatum)
            self.verwaltung.hinzufuegen(mitarbeiter)
            self.ergebnis_text.delete(1.0, tk.END)
            self.ergebnis_text.insert(tk.END, f"Mitarbeiter hinzugefügt:\n{mitarbeiter.zeige_daten()}")
            self.clear_entries()
        else:
            messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
    

    def aktualisieren(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        abteilung = self.abteilung_entry.get()
        gehalt = self.gehalt_entry.get()
        einstellungsdatum = self.einstellungsdatum_entry.get()
        

        if name and position and abteilung and gehalt and einstellungsdatum:
            if self.verwaltung.aktualisieren(name, (position, abteilung, gehalt, einstellungsdatum)):
                self.ergebnis_text.delete(1.0, tk.END)
                self.ergebnis_text.insert(tk.END, f"Mitarbeiter aktualisiert:\n{name}")
                self.clear_entries()
            else:
                messagebox.showerror("Fehler", f"Kein Mitarbeiter mit dem Namen {name} gefunden.")
        else:
            messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
    

    def loeschen(self):
        name = self.name_entry.get()
        

        if name:
            if self.verwaltung.loeschen(name):
                self.ergebnis_text.delete(1.0, tk.END)
                self.ergebnis_text.insert(tk.END, f"Mitarbeiter gelöscht:\n{name}")
                self.clear_entries()
            else:
                messagebox.showerror("Fehler", f"Kein Mitarbeiter mit dem Namen {name} gefunden.")
        else:
            messagebox.showerror("Fehler", "Bitte geben Sie einen Namen ein.")
    

    def suchen(self):
        suchbegriff = self.suchen_entry.get()
        

        if suchbegriff:
            ergebnisse = self.verwaltung.suchen(suchbegriff)
            self.ergebnis_text.delete(1.0, tk.END)
            if ergebnisse:
                for ergebnis in ergebnisse:
                    self.ergebnis_text.insert(tk.END, f"{ergebnis}\n\n")
            else:
                self.ergebnis_text.insert(tk.END, "Keine Ergebnisse gefunden.")
        else:
            messagebox.showerror("Fehler", "Bitte geben Sie einen Suchbegriff ein.")
    

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.abteilung_entry.delete(0, tk.END)
        self.gehalt_entry.delete(0, tk.END)
        self.einstellungsdatum_entry.delete(0, tk.END)
        self.suchen_entry.delete(0, tk.END)


# Hauptprogramm

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()