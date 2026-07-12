# ------------------------------------------------------------
# Dateiname: farbauswahl.py
# Farbauswahl mit Tkinter
#
# Entwickler: Fatih Deniz
# Erstelldatum: 07.07.2026
#
# Funktionen:
# - Auswahl einer Farbe über Radiobuttons
# - Anzeige der ausgewählten Farbe
# - Änderung der Canvas-Hintergrundfarbe
# ------------------------------------------------------------

from tkinter import *


# Deutsche Farbnamen -> Tkinter-Farben
FARBEN = {
    "Rot": "red",
    "Grün": "green",
    "Blau": "blue"
}


def farbe_anzeigen():
    """Zeigt die ausgewählte Farbe an und aktualisiert den Canvas."""

    farbname = farbe.get()

    # Label aktualisieren
    label_ergebnis.config(
        text=f"Ausgewählte Farbe: {farbname}"
    )

    # Canvas-Hintergrund ändern
    canvas.config(bg=FARBEN[farbname])

    # Alten Text löschen
    canvas.delete("text")

    # Passende Schriftfarbe auswählen
    if farbname == "Blau":
        schriftfarbe = "white"
    else:
        schriftfarbe = "black"

    # Farbname im Canvas anzeigen
    canvas.create_text(
        125,
        60,
        text=farbname,
        font=("Arial", 16, "bold"),
        fill=schriftfarbe,
        tags="text"
    )


# ------------------------------------------------------------
# Hauptfenster
# ------------------------------------------------------------

fenster = Tk()
fenster.title("Farbauswahl")
fenster.geometry("400x420")
fenster.resizable(False, False)

# Fenster zentrieren
fenster.columnconfigure(0, weight=1)
fenster.columnconfigure(1, weight=1)

# Kontrollvariable
farbe = StringVar(value="Rot")

# Überschrift
Label(
    fenster,
    text="Wähle deine Lieblingsfarbe:",
    font=("Arial", 14, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(15, 15)
)

# Radiobuttons
Radiobutton(
    fenster,
    text="Rot",
    variable=farbe,
    value="Rot"
).grid(row=1, column=0, columnspan=2)

Radiobutton(
    fenster,
    text="Grün",
    variable=farbe,
    value="Grün"
).grid(row=2, column=0, columnspan=2)

Radiobutton(
    fenster,
    text="Blau",
    variable=farbe,
    value="Blau"
).grid(row=3, column=0, columnspan=2)

# Button
Button(
    fenster,
    text="Bestätigen",
    width=15,
    command=farbe_anzeigen
).grid(
    row=4,
    column=0,
    columnspan=2,
    pady=15
)

# Ergebnis-Label
label_ergebnis = Label(
    fenster,
    text="Ausgewählte Farbe: Rot",
    font=("Arial", 12)
)

label_ergebnis.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=10
)

# Canvas
canvas = Canvas(
    fenster,
    width=250,
    height=120,
    bg="red",
    bd=2,
    relief="groove"
)

canvas.grid(
    row=6,
    column=0,
    columnspan=2,
    pady=15
)

# Starttext im Canvas
canvas.create_text(
    125,
    60,
    text="Rot",
    font=("Arial", 16, "bold"),
    fill="black",
    tags="text"
)

# Ereignisschleife
fenster.mainloop()