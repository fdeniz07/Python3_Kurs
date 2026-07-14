# ------------------------------------------------------------
# Dateiname: farbtester.pyw
# Hex-Farbtester mit Tkinter
#
# Entwickler: Fatih Deniz
# Erstelldatum: 09.07.2026
#
# Beschreibung:
# Mit den drei Schaltflächen wird ein Hex-Farbcode erstellt.
# Die ausgewählte Farbe wird als Vorschau angezeigt.
# ------------------------------------------------------------

from tkinter import Button, Label, Tk, Frame


class Taste(Button):
    ziffern = "0123456789ABCDEF"

    def __init__(self, app, text):
        self.i = 0
        self.app = app

        self.frame = Frame(app)
        self.frame.pack(pady=5)

        Label(
            self.frame,
            text=text,
            width=8,
            font=("Arial", 11, "bold")
        ).pack(side="left", padx=5)

        Button.__init__(
            self,
            master=self.frame,
            text=self.ziffern[self.i],
            command=self.druecken,
            font=("Arial", 16, "bold"),
            width=3
        )

        self.pack(side="left")

    def druecken(self):
        self.i = (self.i + 1) % 16
        self.config(text=self.ziffern[self.i])
        self.app.farbe_anzeigen()

    def ziffer(self):
        return self.ziffern[self.i]


class App(Tk):

    def __init__(self):
        super().__init__()

        self.title("Hex-Farbtester")
        self.geometry("360x420")
        self.resizable(False, False)

        Label(
            self,
            text="Hex-Farbtester",
            font=("Arial", 18, "bold")
        ).pack(pady=(10, 5))

        Label(
            self,
            text="Mit den Schaltflächen wird ein Hex-Farbcode erstellt.",
            font=("Arial", 10)
        ).pack(pady=(0, 15))

        self.tasten = [
            Taste(self, "Rot"),
            Taste(self, "Grün"),
            Taste(self, "Blau")
        ]

        self.label_code = Label(
            self,
            text="HEX: #000",
            font=("Consolas", 14, "bold")
        )
        self.label_code.pack(pady=(15, 5))

        self.label_rgb = Label(
            self,
            text="RGB: (0, 0, 0)",
            font=("Arial", 11)
        )
        self.label_rgb.pack()

        self.label = Label(
            self,
            width=22,
            height=8,
            relief="groove",
            bd=2,
            bg="#000"
        )
        self.label.pack(pady=20)

        self.farbe_anzeigen()

        self.mainloop()

    def farbe_anzeigen(self):

        r, g, b = [t.ziffer() for t in self.tasten]

        code = "#" + r + g + b

        self.label.config(bg=code)

        self.label_code.config(
            text=f"HEX: {code.upper()}"
        )

        rot = int(r * 2, 16)
        gruen = int(g * 2, 16)
        blau = int(b * 2, 16)

        self.label_rgb.config(
            text=f"RGB: ({rot}, {gruen}, {blau})"
        )


App()