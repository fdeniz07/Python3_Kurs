'''
Aufgabe: Grafische Benutzeroberfläche
Entwickle ein Python-Skript, das ein einfaches GUI (Graphical User Interface) mit Tkinter erstellt. Deine Anwendung soll ein kleines Quiz darstellen, in dem der Nutzer zwischen drei Optionen (A, B, C) mittels Radiobuttons wählen kann. Jede Option soll eine andere Farbe repräsentieren (Rot, Grün, Blau). Nach der Auswahl und einem Klick auf eine Schaltfläche "Bestätigen" soll das Hintergrundfarbe des Anwendungsfensters entsprechend der Auswahl geändert werden. Nutze dazu die Kontrollvariable der Radiobuttons, um die Auswahl zu ermitteln und die Hintergrundfarbe anzupassen. Implementiere zudem eine Funktion, die die Farbänderung durchführt. Die GUI soll außerdem eine Schaltfläche "Zurücksetzen" enthalten, die die Hintergrundfarbe auf die Standardfarbe zurücksetzt und die Auswahl der Radiobuttons aufhebt.

a) Definiere die GUI-Elemente und die notwendigen Variablen.

b) Implementiere die Funktion zur Änderung der Hintergrundfarbe basierend auf der Auswahl.

c) Füge Eventhandler für die Schaltflächen "Bestätigen" und "Zurücksetzen" hinzu.

d) Organisiere die Widgets im Fenster mithilfe des Raster-Layouts. 
'''

import tkinter as tk


# Hintergrundfarbe ändern
def farbe_aendern():
    auswahl = farbe.get()

    if auswahl == "Rot":
        fenster.configure(bg="red")
    elif auswahl == "Grün":
        fenster.configure(bg="green")
    elif auswahl == "Blau":
        fenster.configure(bg="blue")


# Fenster zurücksetzen
def zuruecksetzen():
    fenster.configure(bg=standardfarbe)
    farbe.set("") # farbe.set(None) funktioniert nicht, daher leeren wir die Variable mit einem leeren String


# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Farbquiz")
fenster.geometry("350x250")

# Standardfarbe speichern
standardfarbe = fenster.cget("bg")

# Kontrollvariable
farbe = tk.StringVar()
farbe.set("")

# Überschrift
label = tk.Label(
    fenster,
    text="Wähle eine Farbe:",
    font=("Arial", 14)
)
label.grid(row=0, column=0, columnspan=2, pady=10)

# Radiobuttons
radio_rot = tk.Radiobutton(
    fenster,
    text="A - Rot",
    variable=farbe,
    value="Rot"
)
radio_rot.grid(row=1, column=0, sticky="w", padx=20)

radio_gruen = tk.Radiobutton(
    fenster,
    text="B - Grün",
    variable=farbe,
    value="Grün"
)
radio_gruen.grid(row=2, column=0, sticky="w", padx=20)

radio_blau = tk.Radiobutton(
    fenster,
    text="C - Blau",
    variable=farbe,
    value="Blau"
)
radio_blau.grid(row=3, column=0, sticky="w", padx=20)

# Buttons
button_bestaetigen = tk.Button(
    fenster,
    text="Bestätigen",
    command=farbe_aendern
)
button_bestaetigen.grid(row=4, column=0, padx=10, pady=15)

button_zuruecksetzen = tk.Button(
    fenster,
    text="Zurücksetzen",
    command=zuruecksetzen
)
button_zuruecksetzen.grid(row=4, column=1, padx=10, pady=15)

# Ereignisschleife starten
fenster.mainloop()