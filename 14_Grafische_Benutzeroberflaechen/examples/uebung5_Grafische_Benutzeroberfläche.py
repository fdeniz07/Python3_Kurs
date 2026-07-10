'''
Aufgabe: Grafische Benutzeroberfläche
Entwickle ein Python-Programm, das ein Tkinter-Anwendungsfenster erstellt.
In diesem Fenster sollen Nutzer*innen aus drei verschiedenen Obstsorten (Äpfel, Bananen, Orangen) 
über Radiobuttons auswählen können. Nach der Auswahl und einem Klick auf eine Schaltfläche "Bestätigen" 
soll der ausgewählte Wert in einem Label angezeigt werden. Zusätzlich soll eine Funktion implementiert werden, 
die es ermöglicht, über eine Dialogbox eine Textdatei zu öffnen, deren Inhalt dann in einem Text-Widget dargestellt wird. 
Die Anwendung soll auch einen Button zum Schließen des Fensters enthalten. Berücksichtige die Verwendung von Threads, 
um sicherzustellen, dass die GUI reaktionsfähig bleibt, während die Datei geladen wird. 
'''


import tkinter as tk
from tkinter import filedialog
import threading


# Ausgewählte Obstsorte anzeigen
def bestaetigen():
    ausgabe_label.config(text=f"Ausgewählt: {obst.get()}")


# Datei laden (läuft im Hintergrund)
def datei_laden():
    dateiname = filedialog.askopenfilename(
        title="Textdatei auswählen",
        filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")]
    )

    if dateiname:
        with open(dateiname, "r", encoding="utf-8") as datei:
            inhalt = datei.read()

        # GUI im Hauptthread aktualisieren
        fenster.after(0, text_anzeigen, inhalt)


# Text im Text-Widget anzeigen
def text_anzeigen(inhalt):
    textfeld.delete("1.0", tk.END)
    textfeld.insert(tk.END, inhalt)


# Thread starten
def datei_oeffnen():
    thread = threading.Thread(target=datei_laden)
    thread.daemon = True
    thread.start()


# Hauptfenster
fenster = tk.Tk()
fenster.title("Obstauswahl")
fenster.geometry("600x450")

# Überschrift
label = tk.Label(
    fenster,
    text="Wähle eine Obstsorte:",
    font=("Arial", 14)
)
label.grid(row=0, column=0, columnspan=2, pady=10)

# Kontrollvariable
obst = tk.StringVar(value="Äpfel")

# Radiobuttons
tk.Radiobutton(
    fenster,
    text="Äpfel",
    variable=obst,
    value="Äpfel"
).grid(row=1, column=0, sticky="w", padx=20)

tk.Radiobutton(
    fenster,
    text="Bananen",
    variable=obst,
    value="Bananen"
).grid(row=2, column=0, sticky="w", padx=20)

tk.Radiobutton(
    fenster,
    text="Orangen",
    variable=obst,
    value="Orangen"
).grid(row=3, column=0, sticky="w", padx=20)

# Bestätigen
button_bestaetigen = tk.Button(
    fenster,
    text="Bestätigen",
    command=bestaetigen
)
button_bestaetigen.grid(row=4, column=0, pady=10)

# Ausgabe
ausgabe_label = tk.Label(
    fenster,
    text="",
    font=("Arial", 12, "bold"),
    fg="blue"
)
ausgabe_label.grid(row=4, column=1)

# Datei öffnen
button_datei = tk.Button(
    fenster,
    text="Datei öffnen",
    command=datei_oeffnen
)
button_datei.grid(row=5, column=0, pady=10)

# Text-Widget
textfeld = tk.Text(
    fenster,
    width=60,
    height=12
)
textfeld.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Schließen
button_schliessen = tk.Button(
    fenster,
    text="Schließen",
    command=fenster.destroy
)
button_schliessen.grid(row=7, column=0, columnspan=2, pady=10)

# Ereignisschleife
fenster.mainloop()