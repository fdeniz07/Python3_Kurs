#----------------------------------------------------------------
# Dateiname: zahlen_regen_pro.pyw
# Ein Spiel: Zufallszahlen fallen von oben nach unten
# und werden mit einem Schläger gefangen. Für jede gefangene
# Zahl gibt es den Zahlenwert als Punkte.
# Negative Zahlen werden vom Punktestand abgezogen.
# Punkte und verbleibende Zeit werden angezeigt.
#--------------------------------------------------------------
# zahlen_regen.pyw
from tkinter import Button, Canvas, Label, Tk, LEFT, RIGHT
from random import choice, randint
from _thread import start_new_thread
from time import sleep

class Zahl:
    def __init__(self, app):                               #1
        self.canvas = app.canvas
        self.schläger = app.schläger
        self.app = app
        self.wert = 0
        self.id = self.canvas.create_text(0, 0, text=' ')                    
   
    def run(self):
        c = self.canvas
        while self.app.go:
            x, y = randint(10, 290), -10
            self.wert = randint(-10, 10)
            c.itemconfigure(self.id, text=str(self.wert))
            c.coords(self.id, x, y)
            x1, y1, x2, y2 = c.coords(self.schläger.id)
            hit = self.id in c.find_overlapping(
                                        x1, y1, x2, y2)
            sleep(randint(0, 30)/10)
            while (y < 220) and not hit:
               sleep(0.05)
               x, y = c.coords(self.id)
               c.move(self.id, 0, 5)
               x1, y1, x2, y2 = c.coords(self.schläger.id)
               hit = self.id in c.find_overlapping(
                                          x1, y1, x2, y2)
            if hit and self.app.go:
                self.app.punkte_vergeben(self.wert)
            if not self.app.go:
                c.coords(self.id, 0, -10)

class Schläger:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 185, 40, 190,
                                          fill='blue')

    def links(self):
        self.canvas.move(self.id, -20, 0)

    def rechts(self):
        self.canvas.move(self.id, 20, 0)


class App():
    def __init__(self):
        self.punkte = 0
        self.go = False
        self.fenster = Tk()
        self.label_punkte = Label(master=self.fenster,
                                  width=20,
                                  font=('Arial', 12),
                                  text='Punkte: 0')
        self.label_uhr = Label(master=self.fenster,
                               width=20,
                               font=('Arial', 12))
        self.canvas = Canvas(self.fenster, bg='white',
                             width=300, height=200)
        self.schläger = Schläger(self.canvas)
        self.zahlen = [Zahl(self) for i in range(12)]
        self.b_start = Button(master=self.fenster,
                              text='Start',
                              command=self.start)
        self.b_links = Button(master=self.fenster,
                              text='<-',
                              command=self.schläger.links)
        self.b_rechts = Button(master=self.fenster,
                               text='->',
                               command=self.schläger.rechts)
        self.label_uhr.pack(padx=5, pady=5)
        self.label_punkte.pack(padx=5, pady=5)
        self.canvas.pack()
        self.b_start.pack(padx=5, pady=5, side=LEFT)
        self.b_links.pack(padx=5, pady=5, side=LEFT)
        self.b_rechts.pack(padx=5, pady=5, side=LEFT)
        self.fenster.mainloop()

    def punkte_vergeben(self, punkte):
        self.punkte += punkte
        self.label_punkte.config(
                        text='Punkte: ' +str(self.punkte))

    def zeitkontrolle(self):
        zeit = 10
        while zeit > 0:
            self.label_uhr.config(
                            text=str(zeit) + ' Sekunden')
            sleep(1)
            zeit -=1
            self.label_uhr.config(text='Spielende')
        self.go = False

    def start(self):
        self.punkte = 0
        self.label_punkte.config(text='Punkte: 0')
        self.go = True
        for zahl in self.zahlen:
            start_new_thread(zahl.run, ())
        start_new_thread(self.zeitkontrolle, ())
        
App()

        
            

        

