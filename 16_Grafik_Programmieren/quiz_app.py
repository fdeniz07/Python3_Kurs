# ------------------------------------------------------------
# Dateiname: quiz_app.py
# Einfaches Quiz mit Tkinter
#
# Entwickler: Fatih Deniz
# Erstelldatum: 07.07.2026
#
# Funktionen:
# - Quiz mit Radiobuttons
# - 30-Sekunden-Timer
# - Ergebnisse als JSON speichern und laden
# ------------------------------------------------------------

import json
import threading
import time
from tkinter import *
from tkinter import filedialog, messagebox

FRAGEN = [
    {"frage":"Was ist die Hauptstadt von Deutschland?",
     "antworten":["Berlin","Paris","Rom"],
     "richtig":"Berlin"},
    {"frage":"Wie viele Tage hat eine Woche?",
     "antworten":["5","7","10"],
     "richtig":"7"},
    {"frage":"Welche Sprache wird mit Python programmiert?",
     "antworten":["Programmiersprache","Datenbank","Browser"],
     "richtig":"Programmiersprache"},
]

# Globale Variablen
frage_index = -1
punkte = 0
sekunden = 30
timer_laeuft = False
radiobuttons = []

# Timer-Funktion
def timer():
    global sekunden, timer_laeuft
    while timer_laeuft and sekunden >= 0:
        fenster.after(0, lambda s=sekunden: label_timer.config(text=f"Zeit: {s} s"))
        time.sleep(1)
        sekunden -= 1
    if timer_laeuft:
        fenster.after(0, naechste_frage)

# Timer starten
def timer_starten():
    global sekunden, timer_laeuft
    timer_laeuft = False
    sekunden = 30
    timer_laeuft = True
    threading.Thread(target=timer, daemon=True).start()

# Neue Frage laden
def frage_anzeigen():
    daten = FRAGEN[frage_index]
    label_frage.config(text=daten["frage"])
    antwort.set(daten["antworten"][0])
    for rb, txt in zip(radiobuttons, daten["antworten"]):
        rb.config(text=txt, value=txt)
    timer_starten()

# Nächste Frage anzeigen
def naechste_frage():
    global frage_index, punkte, timer_laeuft
    if frage_index >= 0 and antwort.get() == FRAGEN[frage_index]["richtig"]:
        punkte += 1
    timer_laeuft = False
    frage_index += 1
    if frage_index >= len(FRAGEN):
        label_frage.config(text="Quiz beendet!")
        label_timer.config(text="")
        messagebox.showinfo("Ergebnis", f"Punkte: {punkte}/{len(FRAGEN)}")
        return
    frage_anzeigen()

# Ergebnisse als JSON speichern und laden
def speichern():
    datei = filedialog.asksaveasfilename(defaultextension=".json",
                                         filetypes=[("JSON","*.json")])
    if datei:
        with open(datei,"w",encoding="utf-8") as f:
            json.dump({"Punkte":punkte,"Fragen":len(FRAGEN)},f,indent=4)
        messagebox.showinfo("Info","Ergebnisse gespeichert.")

# Ergebnisse von JSON-Datei laden
def laden():
    datei = filedialog.askopenfilename(filetypes=[("JSON","*.json")])
    if datei:
        with open(datei,"r",encoding="utf-8") as f:
            daten=json.load(f)
        messagebox.showinfo("Geladene Ergebnisse",
                            f"Punkte: {daten['Punkte']}\nFragen: {daten['Fragen']}")

fenster=Tk()
fenster.title("Quiz App")
fenster.geometry("500x350")

antwort = StringVar(master=fenster)

Label(fenster,text="Einfaches Quiz",font=("Arial",18,"bold")).pack(pady=10)
label_frage=Label(fenster,font=("Arial",13),wraplength=450)
label_frage.pack(pady=10)

# Radiobuttons für die Antworten
for _ in range(3):
    rb=Radiobutton(fenster,variable=antwort,font=("Arial",12))
    rb.pack(anchor="w",padx=40)
    radiobuttons.append(rb)

label_timer=Label(fenster,text="Zeit: 30 s",fg="red",font=("Arial",12))
label_timer.pack(pady=10)

Button(fenster,text="Nächste Frage",command=naechste_frage).pack(pady=3)
Button(fenster,text="Ergebnisse speichern",command=speichern).pack(pady=3)
Button(fenster,text="Ergebnisse laden",command=laden).pack(pady=3)

naechste_frage()
fenster.mainloop()

