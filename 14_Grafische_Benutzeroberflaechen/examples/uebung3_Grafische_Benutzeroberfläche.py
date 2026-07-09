'''
Aufgabe: Grafische Benutzeroberfläche
Entwickle ein Python-Programm, das eine einfache grafische Benutzeroberfläche (GUI) mit dem Modul tkinter erstellt. Dein Programm soll ein Hauptfenster mit dem Titel "Mein erstes GUI-Programm" haben. In diesem Fenster sollen folgende Widgets platziert und konfiguriert werden:

a) Ein Label-Widget, das die Begrüßung "Willkommen zu meinem Programm!" anzeigt. Stelle sicher, dass der Text zentriert ist und eine Schriftgröße von 14 Punkten hat. Die Hintergrundfarbe des Labels soll Gelb ('yellow') und die Textfarbe Blau ('blue') sein.

b) Ein Entry-Widget zur Texteingabe, das mindestens 20 Zeichen breit ist.

c) Zwei Button-Widgets: Der erste Button soll "OK" und der zweite "Abbrechen" beschriftet sein. Wenn der "OK"-Button gedrückt wird, soll das Programm in der Konsole den im Entry-Widget eingegebenen Text ausgeben. Beim Drücken des "Abbrechen"-Buttons soll das Programm beendet werden.

d) Platziere die Widgets in einem Raster-Layout, sodass das Label-Widget in der ersten Zeile (Zeile 0), das Entry-Widget in der zweiten Zeile (Zeile 1) und beide Button-Widgets nebeneinander in der dritten Zeile (Zeile 2) angezeigt werden. 
'''

import tkinter as tk


# Funktion für den OK-Button
def ok_geklickt():
    print(entry.get())


# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Mein erstes GUI-Programm")

# Label
label = tk.Label(
    fenster,
    text="Willkommen zu meinem Programm!",
    font=("Arial", 14),
    bg="yellow",
    fg="blue",
    width=30
)
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entry
entry = tk.Entry(
    fenster,
    width=20,
    font=("Arial", 12)
)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# OK-Button
button_ok = tk.Button(
    fenster,
    text="OK",
    width=10,
    command=ok_geklickt
)
button_ok.grid(row=2, column=0, padx=10, pady=10)

# Abbrechen-Button
button_abbrechen = tk.Button(
    fenster,
    text="Abbrechen",
    width=10,
    command=fenster.destroy
)
button_abbrechen.grid(row=2, column=1, padx=10, pady=10)

# Ereignisschleife starten
fenster.mainloop()