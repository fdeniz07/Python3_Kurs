'''
Aufgabe: Grafik programmieren
Erstelle ein einfaches Python-Programm mit Tkinter, das folgende Elemente enthält:

a) Ein Hauptfenster mit dem Titel "Mein GUI-Programm".

b) Im Hauptfenster soll ein Label mit dem Text "Hallo Welt!" angezeigt werden.

c) Unter dem Label soll eine Schaltfläche (Button) platziert werden, die beim Klicken den Text des Labels in "Button wurde geklickt!" ändert.

d) Füge einen Radiobutton hinzu, der es ermöglicht, zwischen zwei Farben für den Hintergrund des Labels zu wechseln: Rot und Blau. Die Auswahl des Radiobuttons soll sofort den Hintergrund des Labels entsprechend der Auswahl ändern.

e) Verwende ein Canvas-Widget, um eine einfache Linie und einen Kreis zu zeichnen.
'''

import tkinter as tk


# Label-Text ändern
def button_geklickt():
    label.config(text="Button wurde geklickt!")


# Hintergrundfarbe ändern
def farbe_aendern():
    label.config(bg=farbe.get())


# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Mein GUI-Programm")
fenster.geometry("400x400")

# Label
label = tk.Label(
    fenster,
    text="Hallo Welt!",
    font=("Arial", 14),
    width=25,
    bg="white"
)
label.pack(pady=10)

# Button
button = tk.Button(
    fenster,
    text="Klick mich!",
    command=button_geklickt
)
button.pack(pady=10)

# Radiobuttons
farbe = tk.StringVar(value="red")

radio_rot = tk.Radiobutton(
    fenster,
    text="Rot",
    variable=farbe,
    value="red",
    command=farbe_aendern
)
radio_rot.pack()

radio_blau = tk.Radiobutton(
    fenster,
    text="Blau",
    variable=farbe,
    value="blue",
    command=farbe_aendern
)
radio_blau.pack()

# Anfangsfarbe setzen
farbe_aendern()

# Canvas
canvas = tk.Canvas(
    fenster,
    width=300,
    height=150,
    bg="white"
)
canvas.pack(pady=20)

# Linie zeichnen
canvas.create_line(30, 30, 270, 30, width=3)

# Kreis zeichnen
canvas.create_oval(100, 60, 200, 160, outline="black", width=3)

# Ereignisschleife starten
fenster.mainloop()