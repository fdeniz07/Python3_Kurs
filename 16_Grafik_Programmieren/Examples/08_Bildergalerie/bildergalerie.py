#----------------------------------------------------------------
# Dateiname: bildergalerie.pyw
# Bildergalerie. Das Programm zeigt Zufallsfotos.
#
# Bildnachweis:
# London: CC BY-SA 4.0 2009 Diliff, Wikimedia Commons
# Prag: CC BY-SA 4.0 2016 DXR, Wikimedia Commons
# Brüssel: CC BY-SA 4.0 2006 Horst J. Meuter, Wikimedia Commons
#----------------------------------------------------------------
# -------------------------------------------------------------
# Beispiel: Bildergalerie
# Dieses Beispiel zeigt, wie Bilder mit Pillow geladen
# und in einem Tkinter-Fenster angezeigt werden.
# -------------------------------------------------------------

from pathlib import Path
from random import choice
from tkinter import Tk, Label, Button

from PIL import Image, ImageTk

# Ordner des Programms
ordner = Path(__file__).parent

# Breite der angezeigten Bilder
BREITE = 400

# Bilder mit Beschreibung
BILDER = [
    (ordner / "atomium.jpg", "📍 Atomium (Brüssel)"),
    (ordner / "london.jpg", "📍 Tower Bridge (London)"),
    (ordner / "prag.jpg", "📍 Karlsbrücke (Prag)")
]


def neues_bild():
    """Lädt ein zufälliges Bild und zeigt es an."""

    global bild_tk

    pfad, beschreibung = choice(BILDER)

    bild_pil = Image.open(pfad)

    original_breite, original_hoehe = bild_pil.size

    neue_hoehe = int(BREITE / original_breite * original_hoehe) # Neue Höhe berechnen, um das Seitenverhältnis beizubehalten

    bild_pil = bild_pil.resize((BREITE, neue_hoehe)) # Bild auf die neue Größe skalieren

    bild_tk = ImageTk.PhotoImage(bild_pil) # Tkinter-kompatibles Bildobjekt erstellen

    label_bild.config(image=bild_tk) # Das Bild im Label anzeigen

    label_info.config(
        text=f"{beschreibung}\n"
             f"Originalgröße: {original_breite} × {original_hoehe} Pixel"
    ) # Die Bildbeschreibung und Originalgröße im Label anzeigen


# -------------------------------------------------------------
# Hauptfenster
# -------------------------------------------------------------

fenster = Tk()
fenster.title("Bildergalerie")

# Bild anzeigen
label_bild = Label(fenster)
label_bild.pack(padx=10, pady=(10, 5))

# Bildinformationen
label_info = Label(
    fenster,
    text="",
    font=("Arial", 12, "bold"),
    fg="darkblue",
    justify="center"
)
label_info.pack(pady=(0, 10))

# Button
button_neu = Button(
    fenster,
    text="Neues Bild",
    font=("Arial", 14, "bold"),
    width=15,
    command=neues_bild
)
button_neu.pack(pady=(0, 10))

# Erstes Bild anzeigen
neues_bild()

# Ereignisschleife starten
fenster.mainloop()