
# ------------------------------------------------------------
# Dateiname: zahlen_regen_pro_v2.pyw
# Modernisierte Version des Zahlenregen-Spiels
# Entwickler: Fatih Deniz
# ------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
from random import randint
import threading
import time

SPIELZEIT = 10

class Zahl:

    def __init__(self, app):
        self.app = app
        self.canvas = app.canvas
        self.id = self.canvas.create_text(0, -20, font=("Arial", 14, "bold"))
        self.wert = 0

    def run(self):
        while True:
            while not self.app.go:
                time.sleep(0.2)

            x = randint(20, 380)
            y = -20
            self.wert = randint(-10, 10)

            farbe = "green" if self.wert > 0 else "red"
            if self.wert == 0:
                farbe = "black"

            self.canvas.after(
                0,
                lambda x=x, y=y, f=farbe, w=self.wert:
                    (
                        self.canvas.itemconfig(self.id, text=str(w), fill=f),
                        self.canvas.coords(self.id, x, y)
                    )
            )

            while self.app.go and y < 260:
                time.sleep(0.05)
                y += 5

                def move():
                    self.canvas.coords(self.id, x, y)
                self.canvas.after(0, move)

                sx1, sy1, sx2, sy2 = self.canvas.coords(self.app.schlaeger)

                if self.id in self.canvas.find_overlapping(sx1, sy1, sx2, sy2):
                    self.app.punkte += self.wert
                    self.canvas.after(0, self.app.update_punkte)
                    break


class App:

    def __init__(self):

        self.go = False
        self.punkte = 0

        self.fenster = Tk()
        self.fenster.title("Zahlenregen")
        self.fenster.geometry("470x430")
        self.fenster.resizable(False, False)

        Label(
            self.fenster,
            text="🎮 Zahlenregen",
            font=("Arial",18,"bold")
        ).pack(pady=(10,2))

        Label(
            self.fenster,
            text="Fange möglichst viele positive Zahlen!",
            font=("Arial",10)
        ).pack()

        info = Frame(self.fenster)
        info.pack(pady=10)

        self.label_punkte = Label(info,text="⭐ Punkte: 0",font=("Arial",12))
        self.label_punkte.pack(side=LEFT,padx=20)

        self.label_zeit = Label(info,text="⏱ Zeit: 10 s",font=("Arial",12))
        self.label_zeit.pack(side=LEFT,padx=20)

        self.canvas = Canvas(self.fenster,width=420,height=260,bg="white",bd=2,relief="groove")
        self.canvas.pack()

        self.schlaeger = self.canvas.create_rectangle(
            180,240,260,250,
            fill="#0078D7",
            outline="navy",
            width=2
        )

        buttons = Frame(self.fenster)
        buttons.pack(pady=10)

        Button(buttons,text="▶ Spiel starten",command=self.start,width=14).pack(side=LEFT,padx=5)
        Button(buttons,text="◀",command=self.links,width=5).pack(side=LEFT,padx=5)
        Button(buttons,text="▶",command=self.rechts,width=5).pack(side=LEFT,padx=5)

        self.fenster.bind("<Left>", lambda e:self.links())
        self.fenster.bind("<Right>", lambda e:self.rechts())

        self.zahlen = [Zahl(self) for _ in range(8)]

        for z in self.zahlen:
            threading.Thread(target=z.run,daemon=True).start()

        self.fenster.mainloop()

    def links(self):
        self.canvas.move(self.schlaeger,-20,0)

    def rechts(self):
        self.canvas.move(self.schlaeger,20,0)

    def update_punkte(self):
        self.label_punkte.config(text=f"⭐ Punkte: {self.punkte}")

    def timer(self):
        zeit = SPIELZEIT
        while zeit >= 0 and self.go:
            self.label_zeit.after(0, lambda t=zeit:self.label_zeit.config(text=f"⏱ Zeit: {t} s"))
            time.sleep(1)
            zeit -= 1

        self.go = False

        self.fenster.after(
            0,
            lambda: messagebox.showinfo(
                "Spiel beendet",
                f"Endstand: {self.punkte} Punkte"
            )
        )

    def start(self):
        self.go = False
        time.sleep(0.1)
        self.punkte = 0
        self.update_punkte()
        self.canvas.coords(self.schlaeger,180,240,260,250)
        self.go = True
        threading.Thread(target=self.timer,daemon=True).start()


App()
