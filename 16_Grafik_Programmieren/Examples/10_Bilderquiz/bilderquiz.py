
"""
Dateiname: bilderquiz.py
Mini-Projekt: Städte Quiz (Online Edition)

Benötigte Pakete:
pip install pillow requests
"""

import random
import threading
from io import BytesIO

import requests
import urllib3
from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk, Label, Button, Radiobutton, StringVar, messagebox, ttk

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BREITE = 500
FARBE = "#4F81BD"

STAEDTE = [
    {
        "stadt": "Berlin",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/25/Museo_Bode%2C_Berl%C3%ADn%2C_Alemania%2C_2016-04-22%2C_DD_30.jpg",
    },
    {
        "stadt": "Prag",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/72/North_view_of_Charles_Bridge_from_M%C3%A1nes%C5%AFv_most%2C_Prague_20160808_1.jpg",
    },
    {
        "stadt": "London",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/97/Palace_of_Westminster%2C_London_-_Feb_2007.jpg",
    },
    {
        "stadt": "Brüssel",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/94/Atomium%2C_Br%C3%BCssel_1.jpg",
    },
]

punkte = 0
fragen = 0
richtige_stadt = ""
bild_tk = None
fenster = None
progress = None
status = None
label_bild = None
antwort = None
radiobuttons = []
label_ergebnis = None
label_punkte = None


def erzeuge_fallback_bild(text: str) -> Image.Image:
    bild = Image.new("RGB", (BREITE, 300), color="white")
    draw = ImageDraw.Draw(bild)
    draw.rectangle((10, 10, BREITE - 10, 290), outline="gray", width=3)
    draw.text((40, 120), text, fill="black")
    return bild


def lade_bild(url: str) -> Image.Image:
    antwort = requests.get(url, timeout=20, verify=False)
    antwort.raise_for_status()
    bild = Image.open(BytesIO(antwort.content)).convert("RGB")
    breite, hoehe = bild.size
    neue_hoehe = max(1, int(BREITE / breite * hoehe))
    return bild.resize((BREITE, neue_hoehe))


def neue_frage() -> None:
    if progress is None or status is None:
        return

    progress.start(10)
    status.config(text="Bild wird geladen ...")
    threading.Thread(target=_lade_frage, daemon=True).start()


def _lade_frage() -> None:
    global richtige_stadt, bild_tk

    try:
        eintrag = random.choice(STAEDTE)
        richtige_stadt = eintrag["stadt"]

        optionen = [x["stadt"] for x in STAEDTE if x["stadt"] != richtige_stadt]
        random.shuffle(optionen)
        optionen = optionen[:2] + [richtige_stadt]
        random.shuffle(optionen)

        try:
            bild = lade_bild(eintrag["url"])
        except Exception as ex:
            print(f"Bild konnte nicht geladen werden: {ex}")
            bild = erzeuge_fallback_bild("Bild konnte nicht geladen werden")

        bild_tk = ImageTk.PhotoImage(bild)

        def update() -> None:
            progress.stop()
            status.config(text="Bild erfolgreich geladen.")
            label_bild.config(image=bild_tk)
            antwort.set("")
            for rb, text in zip(radiobuttons, optionen):
                rb.config(text=text, value=text)
            label_ergebnis.config(text="")

        fenster.after(0, update)
    except Exception as ex:
        fenster.after(0, lambda: fehler(ex))


def fehler(ex: Exception) -> None:
    if progress is not None:
        progress.stop()
    if status is not None:
        status.config(text="Fehler beim Laden.")
    messagebox.showerror("Netzwerkfehler", str(ex))


def pruefen() -> None:
    global punkte, fragen

    fragen += 1

    if antwort.get() == richtige_stadt:
        punkte += 1
        label_ergebnis.config(text="✔ Richtig!", fg="green")
    else:
        label_ergebnis.config(
            text=f"✘ Falsch! Richtige Antwort: {richtige_stadt}",
            fg="red",
        )

    label_punkte.config(text=f"Punktestand: {punkte} / {fragen}")


def main() -> None:
    global fenster, progress, status, label_bild, antwort, radiobuttons, label_ergebnis, label_punkte

    fenster = Tk()
    fenster.title("Städte Quiz (Online Edition)")
    fenster.geometry("620x760")
    fenster.configure(bg="white")

    Label(
        fenster,
        text="Städte Quiz 🌍",
        font=("Arial", 22, "bold"),
        bg="white",
        fg=FARBE,
    ).pack(pady=10)

    Label(
        fenster,
        text="Erraten Sie die Stadt auf dem Bild.",
        font=("Arial", 12),
        bg="white",
    ).pack()

    progress = ttk.Progressbar(fenster, mode="indeterminate", length=250)
    progress.pack(pady=5)

    label_bild = Label(fenster, bg="white")
    label_bild.pack(pady=10)

    antwort = StringVar()

    radiobuttons = []
    for _ in range(3):
        rb = Radiobutton(
            fenster,
            variable=antwort,
            bg="white",
            font=("Arial", 13),
            anchor="w",
            width=20,
        )
        rb.pack(anchor="w", padx=40)
        radiobuttons.append(rb)

    Button(
        fenster,
        text="Antwort prüfen",
        font=("Arial", 12, "bold"),
        command=pruefen,
    ).pack(pady=10)

    Button(
        fenster,
        text="Nächste Frage",
        font=("Arial", 12),
        command=neue_frage,
    ).pack()

    label_ergebnis = Label(
        fenster,
        text="",
        font=("Arial", 14, "bold"),
        bg="white",
    )
    label_ergebnis.pack(pady=10)

    label_punkte = Label(
        fenster,
        text="Punktestand: 0 / 0",
        font=("Arial", 12),
        bg="white",
    )
    label_punkte.pack()

    status = Label(
        fenster,
        text="Bereit.",
        relief="sunken",
        anchor="w",
    )
    status.pack(fill="x", side="bottom")

    neue_frage()
    fenster.mainloop()


if __name__ == "__main__":
    main()
