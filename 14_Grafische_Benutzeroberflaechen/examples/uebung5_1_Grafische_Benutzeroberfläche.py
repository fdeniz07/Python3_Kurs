import tkinter as tk
from tkinter import filedialog
from threading import Thread

def datei_laden():
    def laden():
        pfad = filedialog.askopenfilename()
        if pfad:
            with open(pfad, "r", encoding="utf-8") as file:
                text = file.read()
                text_widget.delete('1.0', tk.END)
                text_widget.insert('1.0', text)
    thread = Thread(target=laden)
    thread.start()

def auswahl_anzeigen():
    ausgewaehlte_obstsorte = obst_var.get()
    auswahl_label.config(text="Ausgewählt: " + ausgewaehlte_obstsorte)

fenster = tk.Tk()
fenster.title("Obstauswahl und Dateiöffner")

obst_var = tk.StringVar()
radiobuttons = [("Äpfel", "Äpfel"), ("Bananen", "Bananen"), ("Orangen", "Orangen")]
for obst, value in radiobuttons:
    rb = tk.Radiobutton(fenster, text=obst, variable=obst_var, value=value, command=auswahl_anzeigen)
    rb.pack(anchor=tk.W)

auswahl_label = tk.Label(fenster, text="Bitte wähle eine Obstsorte.")
auswahl_label.pack()

oeffnen_button = tk.Button(fenster, text="Datei öffnen", command=datei_laden)
oeffnen_button.pack()

text_widget = tk.Text(fenster, height=10, width=50)
text_widget.pack()

schliessen_button = tk.Button(fenster, text="Schließen", command=fenster.destroy)
schliessen_button.pack()

fenster.mainloop()
