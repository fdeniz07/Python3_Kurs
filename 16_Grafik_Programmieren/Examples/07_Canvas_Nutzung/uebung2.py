'''
Aufgabe: Grafik programmieren
Erstelle ein einfaches Python-Programm mit Tkinter, das folgende Elemente enthält:

a) Ein Hauptfenster mit dem Titel "Mein GUI-Programm".

b) Im Hauptfenster soll ein Label mit dem Text "Hallo Welt!" angezeigt werden.

c) Unter dem Label soll eine Schaltfläche (Button) platziert werden, die beim Klicken den Text des Labels in "Button wurde geklickt!" ändert.

d) Füge einen Radiobutton hinzu, der es ermöglicht, zwischen zwei Farben für den Hintergrund des Labels zu wechseln: Rot und Blau. Die Auswahl des Radiobuttons soll sofort den Hintergrund des Labels entsprechend der Auswahl ändern.

e) Verwende ein Canvas-Widget, um eine einfache Linie und einen Kreis zu zeichnen.
'''
from tkinter import *

def aendere_label_text():
    label.config(text="Button wurde geklickt!")

def aendere_label_farbe(farbe):
    label.config(bg=farbe)

def zeichne_canvas():
    canvas.create_line(10, 10, 200, 50)
    canvas.create_oval(50, 50, 150, 100, fill="yellow")

fenster = Tk()
fenster.title("Mein GUI-Programm")

label = Label(fenster, text="Hallo Welt!")
label.pack()

button = Button(fenster, text="Klick mich", command=aendere_label_text)
button.pack()

radiobutton_var = StringVar()
radiobutton_var.set("rot")  # Setzt die Standardfarbe auf Rot

radiobutton_rot = Radiobutton(fenster, text="Rot", variable=radiobutton_var, value="red", command=lambda: aendere_label_farbe("red"))
radiobutton_rot.pack()

radiobutton_blau = Radiobutton(fenster, text="Blau", variable=radiobutton_var, value="blue", command=lambda: aendere_label_farbe("blue"))
radiobutton_blau.pack()

canvas = Canvas(fenster, width=200, height=150)
canvas.pack()
zeichne_canvas()

fenster.mainloop()