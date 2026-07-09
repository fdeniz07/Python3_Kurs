'''
Aufgabe: Grafische Benutzeroberfläche
Entwickle ein Python-Programm, das eine grafische Benutzeroberfläche (GUI) mit Tkinter erstellt. Dein Programm soll ein Anwendungsfenster mit folgenden Widgets und Funktionalitäten beinhalten:

a) Ein Eingabefeld (Entry-Widget), in den Benutzerinnen ihren Namen eingeben können.

b) Eine Schaltfläche (Button), die bei Klick eine Begrüßungsnachricht zusammen mit dem eingegebenen Namen in einem Label-Widget anzeigt.

c) Ein Radiobutton-Widget, mit dem Benutzerinnen ihre bevorzugte Begrüßungszeit auswählen können: "Guten Morgen", "Guten Tag", "Guten Abend". Die Auswahl soll die Begrüßungsnachricht beeinflussen.

d) Ein Text-Widget, das als Log dient, in dem jede durchgeführte Begrüßung mit Zeitstempel gespeichert wird.

e) Verwende das Raster-Layout (Grid), um die Widgets im Anwendungsfenster anzuordnen.

f) Implementiere eine Funktion, die die aktuelle Zeit und Datum als String zurückgibt, und verwende diese, um den Zeitstempel im Log zu generieren.

g) Gestalte das Anwendungsfenster und die Widgets ansprechend, indem du Größen, Farben und Schriftarten anpasst. 
'''

import tkinter as tk
from datetime import datetime


# Aktuelles Datum und Uhrzeit zurückgeben
def aktuelle_zeit_als_string():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


# Begrüßung anzeigen und im Log speichern
def begruessen():
    name = entry_name.get().strip() # Leerzeichen entfernen

    if name == "":
        name = "Gast"

    begruessung = auswahl.get()
    text = f"{begruessung}, {name}!"

    label_ausgabe.config(text=text)

    log_text.insert(
        tk.END,
        f"[{aktuelle_zeit_als_string()}] {text}\n"
    )
    log_text.see(tk.END)


# Hauptfenster
fenster = tk.Tk()
fenster.title("Begrüßungsprogramm")
fenster.geometry("600x450")
fenster.configure(bg="#E8F4FA")
fenster.resizable(False, False)

# Überschrift
titel = tk.Label(
    fenster,
    text="Willkommen!",
    font=("Arial", 18, "bold"),
    bg="#E8F4FA",
    fg="darkblue"
)
titel.grid(row=0, column=0, columnspan=2, pady=15)

# Name
label_name = tk.Label(
    fenster,
    text="Name:",
    font=("Arial", 12),
    bg="#E8F4FA"
)
label_name.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_name = tk.Entry(
    fenster,
    font=("Arial", 12),
    width=30
)
entry_name.grid(row=1, column=1, padx=10, pady=10)

# Radiobuttons
auswahl = tk.StringVar()
auswahl.set("Guten Tag")

radio1 = tk.Radiobutton(
    fenster,
    text="Guten Morgen",
    variable=auswahl,
    value="Guten Morgen",
    bg="#E8F4FA",
    font=("Arial", 11)
)
radio1.grid(row=2, column=0, sticky="w", padx=20)

radio2 = tk.Radiobutton(
    fenster,
    text="Guten Tag",
    variable=auswahl,
    value="Guten Tag",
    bg="#E8F4FA",
    font=("Arial", 11)
)
radio2.grid(row=3, column=0, sticky="w", padx=20)

radio3 = tk.Radiobutton(
    fenster,
    text="Guten Abend",
    variable=auswahl,
    value="Guten Abend",
    bg="#E8F4FA",
    font=("Arial", 11)
)
radio3.grid(row=4, column=0, sticky="w", padx=20)

# Button
button = tk.Button(
    fenster,
    text="Begrüßen",
    font=("Arial", 12, "bold"),
    bg="steelblue",
    fg="white",
    command=begruessen
)
button.grid(row=5, column=0, columnspan=2, pady=15)

# Ausgabe
label_ausgabe = tk.Label(
    fenster,
    text="",
    font=("Arial", 14, "bold"),
    fg="green",
    bg="#E8F4FA"
)
label_ausgabe.grid(row=6, column=0, columnspan=2, pady=10)

# Log
label_log = tk.Label(
    fenster,
    text="Begrüßungs-Log:",
    font=("Arial", 12, "bold"),
    bg="#E8F4FA"
)
label_log.grid(row=7, column=0, sticky="nw", padx=10)

log_text = tk.Text(
    fenster,
    width=55,
    height=8,
    font=("Consolas", 10)
)
log_text.grid(row=7, column=1, padx=10, pady=10)

fenster.mainloop()