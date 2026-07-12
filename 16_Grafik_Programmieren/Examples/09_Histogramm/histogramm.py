
# -------------------------------------------------------------
# Dateiname: histogramm.py
# Mini-Projekt: Histogramm Generator mit Tkinter
# -------------------------------------------------------------

from tkinter import (
    Tk, Label, Entry, Button, Canvas,
    messagebox, filedialog
)
from random import randint
from statistics import mean
from PIL import Image, ImageDraw

BREITE = 700
HOEHE = 400

FARBEN = [
    "#DBEAFE",
    "#BFDBFE",
    "#93C5FD",
    "#60A5FA",
    "#3B82F6",
    "#2563EB",
    "#1D4ED8"
]


def daten_einlesen():
    text = eingabe.get().strip()

    if not text:
        messagebox.showwarning(
            "Hinweis",
            "Bitte geben Sie Zahlen ein."
        )
        return None

    try:
        zahlen = [int(x) for x in text.split()]
    except ValueError:
        messagebox.showerror(
            "Fehler",
            "Nur ganze Zahlen sind erlaubt!"
        )
        return None

    if min(zahlen) < 0:
        messagebox.showerror(
            "Fehler",
            "Bitte nur positive Zahlen eingeben."
        )
        return None

    return zahlen


def zeichne_histogramm():
    global letzte_zahlen

    zahlen = daten_einlesen()
    if zahlen is None:
        return

    letzte_zahlen = zahlen

    canvas.delete("all")

    max_wert = max(zahlen)
    balkenbreite = BREITE / (len(zahlen) + 2)
    faktor = 0.75 * HOEHE / max_wert

    canvas.create_line(20, 340, BREITE - 20, 340, width=2)

    for i, wert in enumerate(zahlen):

        x1 = (i + 1) * balkenbreite
        y1 = 340 - wert * faktor
        x2 = x1 + balkenbreite * 0.8
        y2 = 340

        index = int((wert / max_wert) * (len(FARBEN) - 1))
        farbe = FARBEN[index]

        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=farbe,
            outline="black"
        )

        canvas.create_text(
            (x1 + x2) / 2,
            y1 - 10,
            text=str(wert),
            font=("Arial", 10, "bold")
        )

        canvas.create_text(
            (x1 + x2) / 2,
            355,
            text=str(i + 1),
            font=("Arial", 10)
        )

    info.config(
        text=f"Anzahl: {len(zahlen)}    "
             f"Minimum: {min(zahlen)}    "
             f"Maximum: {max(zahlen)}    "
             f"Durchschnitt: {mean(zahlen):.2f}"
    )

    status.config(text="Status: Histogramm erstellt.")


def beispiel():
    eingabe.delete(0, "end")
    eingabe.insert(0, "5 12 8 3 10 7")
    zeichne_histogramm()


def zufall():
    werte = [str(randint(1, 20)) for _ in range(10)]
    eingabe.delete(0, "end")
    eingabe.insert(0, " ".join(werte))
    zeichne_histogramm()


def loeschen():
    global letzte_zahlen
    letzte_zahlen = None
    canvas.delete("all")
    info.config(text="")
    status.config(text="Status: Canvas gelöscht.")


def speichern():
    if letzte_zahlen is None:
        messagebox.showwarning(
            "Hinweis",
            "Bitte zuerst ein Histogramm erzeugen."
        )
        return

    datei = filedialog.asksaveasfilename(
        title="Histogramm speichern",
        defaultextension=".png",
        filetypes=[("PNG", "*.png")]
    )

    if not datei:
        return

    bild = Image.new("RGB", (BREITE, HOEHE), "white")
    draw = ImageDraw.Draw(bild)

    max_wert = max(letzte_zahlen)
    balkenbreite = BREITE / (len(letzte_zahlen) + 2)
    faktor = 0.75 * HOEHE / max_wert

    draw.line((20, 340, BREITE - 20, 340), fill="black", width=2)

    for i, wert in enumerate(letzte_zahlen):

        x1 = (i + 1) * balkenbreite
        y1 = 340 - wert * faktor
        x2 = x1 + balkenbreite * 0.8
        y2 = 340

        index = int((wert / max_wert) * (len(FARBEN) - 1))
        farbe = FARBEN[index]

        draw.rectangle((x1, y1, x2, y2), fill=farbe, outline="black")
        draw.text((x1 + 5, y1 - 15), str(wert), fill="black")

    bild.save(datei)

    status.config(text=f"Status: Gespeichert unter {datei}")


letzte_zahlen = None

fenster = Tk()
fenster.title("Histogramm Generator")
fenster.geometry("760x620")
fenster.resizable(False, False)

Label(
    fenster,
    text="Histogramm Generator",
    font=("Arial", 18, "bold")
).pack(pady=(10, 5))

Label(
    fenster,
    text="Bitte geben Sie ganze Zahlen ein (durch Leerzeichen getrennt).",
    font=("Arial", 11)
).pack()

eingabe = Entry(fenster, width=50, font=("Arial", 12))
eingabe.pack(pady=10)
eingabe.insert(0, "5 12 8 3 10 7")

Button(fenster, text="Histogramm zeichnen", command=zeichne_histogramm).pack(pady=2)
Button(fenster, text="Beispieldaten laden", command=beispiel).pack(pady=2)
Button(fenster, text="Zufallszahlen erzeugen", command=zufall).pack(pady=2)
Button(fenster, text="Histogramm speichern", command=speichern).pack(pady=2)
Button(fenster, text="Canvas löschen", command=loeschen).pack(pady=2)

canvas = Canvas(fenster, width=BREITE, height=HOEHE, bg="white")
canvas.pack(pady=10)

info = Label(fenster, font=("Arial", 11))
info.pack()

status = Label(fenster, text="Status: Bereit.", anchor="w")
status.pack(fill="x", padx=10, pady=5)

zeichne_histogramm()

fenster.mainloop()
