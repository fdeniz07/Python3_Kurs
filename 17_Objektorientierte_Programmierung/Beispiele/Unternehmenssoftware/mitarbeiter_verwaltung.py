'''
Aufgabe: Objektorientierte Programmierung
Du arbeitest als Softwareentwickler in einem Unternehmen, das sich auf die Entwicklung von Unternehmenssoftware 
spezialisiert hat. Dein aktuelles Projekt beinhaltet die Entwicklung einer Anwendung zur Verwaltung 
von Mitarbeiterdaten. Die Anwendung soll es ermöglichen, Mitarbeiterdaten zu erfassen, zu aktualisieren, 
zu löschen und zu durchsuchen. Die Mitarbeiterdaten umfassen Name, Position, Abteilung, Gehalt und Einstellungsdatum.
Du sollst eine objektorientierte Lösung in Python entwerfen, die folgende Anforderungen erfüllt:

a) Entwerfe eine Klasse Mitarbeiter, die die Attribute Name, Position, Abteilung, Gehalt und Einstellungsdatum 
speichert. Implementiere Methoden zum Setzen und Abrufen dieser Attribute sowie eine Methode zeige_daten(), 
die alle Daten eines Mitarbeiters in einem formatierten String ausgibt.

b) Entwickle eine Klasse MitarbeiterVerwaltung, die eine Liste von Mitarbeiter-Objekten verwaltet. 
Diese Klasse soll Methoden zum Hinzufügen, Aktualisieren (basierend auf dem Namen), Löschen (basierend auf dem Namen)
und Suchen (basierend auf dem Namen oder der Abteilung) von Mitarbeitern beinhalten.

c) Implementiere eine einfache Benutzeroberfläche unter Verwendung des tkinter-Moduls, die es dem Benutzer 
ermöglicht, Mitarbeiterdaten einzugeben, zu aktualisieren, zu löschen und zu durchsuchen. Die Benutzeroberfläche 
sollte auch eine Ausgabebereich haben, in dem die Ergebnisse von Suchoperationen oder die Daten eines neu 
hinzugefügten oder aktualisierten Mitarbeiters angezeigt werden.
'''

"""Tkinter-Anwendung zur einfachen Verwaltung von Mitarbeiterdaten."""

from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk


class Mitarbeiter:
    """Speichert die Daten eines einzelnen Mitarbeiters."""

    def __init__(self, name, position, abteilung, gehalt, einstellungsdatum):
        self.name = name
        self.position = position
        self.abteilung = abteilung
        self.gehalt = gehalt
        self.einstellungsdatum = einstellungsdatum

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_abteilung(self, abteilung):
        self.abteilung = abteilung

    def get_abteilung(self):
        return self.abteilung

    def set_gehalt(self, gehalt):
        self.gehalt = gehalt

    def get_gehalt(self):
        return self.gehalt

    def set_einstellungsdatum(self, einstellungsdatum):
        self.einstellungsdatum = einstellungsdatum

    def get_einstellungsdatum(self):
        return self.einstellungsdatum

    def zeige_daten(self):
        """Gibt alle Mitarbeiterdaten als formatierten Text zurück."""
        return (
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
            f"Abteilung: {self.abteilung}\n"
            f"Gehalt: {self.gehalt:.2f} €\n"
            f"Einstellungsdatum: {self.einstellungsdatum:%d.%m.%Y}"
        )


class MitarbeiterVerwaltung:
    """Verwaltet eine Liste von Mitarbeiter-Objekten."""

    def __init__(self):
        self.mitarbeiter_liste = []

    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        if self._mitarbeiter_nach_name(mitarbeiter.get_name()) is not None:
            raise ValueError("Ein Mitarbeiter mit diesem Namen existiert bereits.")
        self.mitarbeiter_liste.append(mitarbeiter)

    def _mitarbeiter_nach_name(self, name):
        """Sucht einen Mitarbeiter anhand des vollständigen Namens."""
        for mitarbeiter in self.mitarbeiter_liste:
            if mitarbeiter.get_name().casefold() == name.casefold():
                return mitarbeiter
        return None

    def mitarbeiter_aktualisieren(
        self, name, position, abteilung, gehalt, einstellungsdatum
    ):
        mitarbeiter = self._mitarbeiter_nach_name(name)
        if mitarbeiter is None:
            raise ValueError("Mitarbeiter wurde nicht gefunden.")

        mitarbeiter.set_position(position)
        mitarbeiter.set_abteilung(abteilung)
        mitarbeiter.set_gehalt(gehalt)
        mitarbeiter.set_einstellungsdatum(einstellungsdatum)
        return mitarbeiter

    def mitarbeiter_loeschen(self, name):
        mitarbeiter = self._mitarbeiter_nach_name(name)
        if mitarbeiter is None:
            raise ValueError("Mitarbeiter wurde nicht gefunden.")

        self.mitarbeiter_liste.remove(mitarbeiter)
        return mitarbeiter

    def suche_nach_name(self, suchbegriff):
        """Findet alle Mitarbeiter, deren Name den Suchbegriff enthält."""
        return [
            mitarbeiter
            for mitarbeiter in self.mitarbeiter_liste
            if suchbegriff.casefold() in mitarbeiter.get_name().casefold()
        ]

    def suche_nach_abteilung(self, abteilung):
        """Findet alle Mitarbeiter einer Abteilung."""
        return [
            mitarbeiter
            for mitarbeiter in self.mitarbeiter_liste
            if abteilung.casefold() == mitarbeiter.get_abteilung().casefold()
        ]


class MitarbeiterVerwaltungApp:
    """Stellt die Benutzeroberfläche für die Mitarbeiterverwaltung bereit."""

    def __init__(self, fenster):
        self.fenster = fenster
        self.verwaltung = MitarbeiterVerwaltung()
        self.eingabefelder = {}

        self.fenster.title("Mitarbeiterverwaltung")
        self.fenster.resizable(False, False)
        self._oberflaeche_erstellen()

    def _oberflaeche_erstellen(self):
        eingabe_rahmen = ttk.LabelFrame(self.fenster, text="Mitarbeiterdaten", padding=10)
        eingabe_rahmen.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        felder = [
            ("name", "Name:"),
            ("position", "Position:"),
            ("abteilung", "Abteilung:"),
            ("gehalt", "Gehalt (€):"),
            ("einstellungsdatum", "Einstellungsdatum (TT.MM.JJJJ):"),
        ]
        for zeile, (feldname, beschriftung) in enumerate(felder):
            ttk.Label(eingabe_rahmen, text=beschriftung).grid(
                row=zeile, column=0, padx=(0, 8), pady=3, sticky="w"
            )
            eingabefeld = ttk.Entry(eingabe_rahmen, width=35)
            eingabefeld.grid(row=zeile, column=1, pady=3, sticky="ew")
            self.eingabefelder[feldname] = eingabefeld

        schaltflaechen_rahmen = ttk.Frame(self.fenster, padding=(10, 0, 10, 10))
        schaltflaechen_rahmen.grid(row=1, column=0, sticky="ew")
        ttk.Button(schaltflaechen_rahmen, text="Hinzufügen", command=self.hinzufuegen).grid(
            row=0, column=0, padx=3
        )
        ttk.Button(schaltflaechen_rahmen, text="Aktualisieren", command=self.aktualisieren).grid(
            row=0, column=1, padx=3
        )
        ttk.Button(schaltflaechen_rahmen, text="Löschen", command=self.loeschen).grid(
            row=0, column=2, padx=3
        )
        ttk.Button(schaltflaechen_rahmen, text="Nach Name suchen", command=self.nach_name_suchen).grid(
            row=0, column=3, padx=3
        )
        ttk.Button(
            schaltflaechen_rahmen,
            text="Nach Abteilung suchen",
            command=self.nach_abteilung_suchen,
        ).grid(row=0, column=4, padx=3)
        ttk.Button(schaltflaechen_rahmen, text="Eingaben leeren", command=self.eingaben_leeren).grid(
            row=0, column=5, padx=3
        )

        ausgabe_rahmen = ttk.LabelFrame(self.fenster, text="Ausgabe", padding=10)
        ausgabe_rahmen.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.ausgabe = tk.Text(ausgabe_rahmen, width=72, height=15, state="disabled")
        self.ausgabe.grid(row=0, column=0)

    def _eingaben_lesen(self):
        """Liest und validiert alle Daten aus den Eingabefeldern."""
        werte = {name: feld.get().strip() for name, feld in self.eingabefelder.items()}
        if not all(werte.values()):
            raise ValueError("Bitte füllen Sie alle Eingabefelder aus.")

        try:
            gehalt = float(werte["gehalt"].replace(",", "."))
        except ValueError as fehler:
            raise ValueError("Das Gehalt muss eine Zahl sein.") from fehler

        if gehalt < 0:
            raise ValueError("Das Gehalt darf nicht negativ sein.")

        try:
            einstellungsdatum = datetime.strptime(
                werte["einstellungsdatum"], "%d.%m.%Y"
            ).date()
        except ValueError as fehler:
            raise ValueError("Datum bitte im Format TT.MM.JJJJ eingeben.") from fehler

        return werte["name"], werte["position"], werte["abteilung"], gehalt, einstellungsdatum

    def _ausgabe_anzeigen(self, titel, mitarbeiter_liste):
        self.ausgabe.config(state="normal")
        self.ausgabe.delete("1.0", tk.END)
        self.ausgabe.insert(tk.END, f"{titel}\n{'=' * len(titel)}\n\n")
        if mitarbeiter_liste:
            self.ausgabe.insert(
                tk.END, "\n\n".join(mitarbeiter.zeige_daten() for mitarbeiter in mitarbeiter_liste)
            )
        else:
            self.ausgabe.insert(tk.END, "Keine passenden Mitarbeiter gefunden.")
        self.ausgabe.config(state="disabled")

    def hinzufuegen(self):
        try:
            mitarbeiter = Mitarbeiter(*self._eingaben_lesen())
            self.verwaltung.mitarbeiter_hinzufuegen(mitarbeiter)
            self._ausgabe_anzeigen("Mitarbeiter hinzugefügt", [mitarbeiter])
            self.eingaben_leeren()
        except ValueError as fehler:
            messagebox.showerror("Eingabefehler", str(fehler))

    def aktualisieren(self):
        try:
            daten = self._eingaben_lesen()
            mitarbeiter = self.verwaltung.mitarbeiter_aktualisieren(*daten)
            self._ausgabe_anzeigen("Mitarbeiter aktualisiert", [mitarbeiter])
        except ValueError as fehler:
            messagebox.showerror("Aktualisierung nicht möglich", str(fehler))

    def loeschen(self):
        name = self.eingabefelder["name"].get().strip()
        if not name:
            messagebox.showerror("Eingabefehler", "Bitte geben Sie einen Namen ein.")
            return

        try:
            mitarbeiter = self.verwaltung.mitarbeiter_loeschen(name)
            self._ausgabe_anzeigen("Mitarbeiter gelöscht", [mitarbeiter])
            self.eingaben_leeren()
        except ValueError as fehler:
            messagebox.showerror("Löschen nicht möglich", str(fehler))

    def nach_name_suchen(self):
        suchbegriff = self.eingabefelder["name"].get().strip()
        if not suchbegriff:
            messagebox.showerror("Eingabefehler", "Bitte geben Sie einen Namen oder Namensanteil ein.")
            return
        self._ausgabe_anzeigen(
            f"Suchergebnis für Name: {suchbegriff}",
            self.verwaltung.suche_nach_name(suchbegriff),
        )

    def nach_abteilung_suchen(self):
        abteilung = self.eingabefelder["abteilung"].get().strip()
        if not abteilung:
            messagebox.showerror("Eingabefehler", "Bitte geben Sie eine Abteilung ein.")
            return
        self._ausgabe_anzeigen(
            f"Suchergebnis für Abteilung: {abteilung}",
            self.verwaltung.suche_nach_abteilung(abteilung),
        )

    def eingaben_leeren(self):
        for eingabefeld in self.eingabefelder.values():
            eingabefeld.delete(0, tk.END)


if __name__ == "__main__":
    hauptfenster = tk.Tk()
    MitarbeiterVerwaltungApp(hauptfenster)
    hauptfenster.mainloop()
