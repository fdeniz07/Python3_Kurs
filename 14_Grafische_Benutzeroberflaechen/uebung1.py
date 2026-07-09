'''
Aufgabe: Grafische Benutzeroberfläche
Erstelle ein Python-Programm, das ein Tkinter-Anwendungsfenster mit folgenden Widgets und Funktionalitäten erzeugt:

a) Ein Label-Widget, das "Hallo Welt!" anzeigt. Verwende dabei eine Schriftart deiner Wahl mit einer Größe von 14 Punkten.

b) Ein Entry-Widget, in das Nutzer Text eingeben können.

c) Zwei Button-Widgets: Der erste Button soll den Text im Entry-Widget löschen, wenn er geklickt wird. Der zweite Button soll das Anwendungsfenster schließen.

d) Erstelle eine Liste von Tupeln, die jeweils die Texte für die Buttons und die zugehörigen Funktionen (zum Löschen des Textes und zum Schließen des Fensters) 
enthalten. Verwende anschließend eine Schleife, um basierend auf dieser Liste die Buttons ins Anwendungsfenster einzufügen.

e) Gestalte das Anwendungsfenster so, dass das Label oben erscheint, das Entry-Widget darunter und die Buttons am unteren Rand des Fensters angeordnet sind.

f) Verwende die pack()-Methode für das Layoutmanagement aller Widgets.

g) Schreibe Kommentare zu deinem Code, um die Funktionsweise der verschiedenen Teile zu erklären.

h) Stelle sicher, dass das Programm fehlerfrei läuft und alle Widgets wie beschrieben funktionieren. 
'''



import tkinter as tk


fenster=tk.Tk()
fenster.title("Übung 1")
fenster.configure(bg="blue")
fenster.geometry("400x200")

label=tk.Label(
    master=fenster,
    text="Hallo Welt!",
    justify="center",
    font=("Arial",14),
    fg="red"
)

eingabe = tk.Entry(
    master=fenster,
    width=20
)

button_delete=tk.Button(
    fenster,
    text="Eingabe Löschen",
    command=lambda: eingabe.delete(0, tk.END)
)


button_close=tk.Button(
    fenster,
    text="Schließen",
    command=fenster.destroy
)

label.pack()
eingabe.pack()
button_delete.pack()
button_close.pack()


fenster.mainloop()