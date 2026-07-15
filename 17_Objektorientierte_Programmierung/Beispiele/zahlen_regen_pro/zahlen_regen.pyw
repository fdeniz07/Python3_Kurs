#----------------------------------------------------------------
# Dateiname: zahlen_regen.pyw
# Ein Spiel: Zufallszahlen fallen von oben nach unten
# und werden mit einem Schläger gefangen. Für jede gefangene
# Zahl gibt es den Zahkenwert als Punkte.
# Negative Zahlen werden vom Punktestand abgezogen.
#----------------------------------------------------------------
# zahlen_regen.pyw
from tkinter import Button, Canvas, Label, Tk, LEFT, RIGHT
from random import choice, randint
from _thread import start_new_thread


from time import sleep

class Zahl:
    def __init__(self, app):             #1
        self.canvas = app.canvas
        self.schläger = app.schläger
        self.wert = 0
        self.id = self.canvas.create_text(0, 0, text=' ')                    
        start_new_thread(self.run, ())                   #2
   
    def run(self):
        c = self.canvas
        while True:
            x, y = randint(10, 290), -10
            self.wert = randint(-10, 10)
            c.itemconfigure(self.id, text=str(self.wert))
            c.coords(self.id, x, y)
            x1, y1, x2, y2 = c.coords(self.schläger.id)
            hit = self.id in c.find_overlapping(
                                        x1, y1, x2, y2)
            sleep(randint(0, 30)/10)
            while (y < 200) and not hit:
               sleep(0.05)
               x, y = c.coords(self.id)
               c.move(self.id, 0, 5)
               x1, y1, x2, y2 = c.coords(self.schläger.id)
               hit = self.id in c.find_overlapping(
                                          x1, y1, x2, y2)

class Schläger:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 185, 40, 190)

    def links(self):
        self.canvas.move(self.id, -20, 0)

    def rechts(self):
        self.canvas.move(self.id, 20, 0)    

class App():
    def __init__(self):
        self.punkte = 0
        self.fenster = Tk()
        self.canvas = Canvas(self.fenster,
                             width=300, height=200)
        self.schläger = Schläger(self.canvas)
        for i in range(12):
            Zahl(self)
        self.b_links = Button(master=self.fenster,
                              text='<-',
                              command=self.schläger.links)
        self.b_rechts = Button(master=self.fenster,
                               text='->',
                               command=self.schläger.rechts)
        self.canvas.pack()
        self.b_links.pack(padx=5, pady=5, side=LEFT)
        self.b_rechts.pack(padx=5, pady=5, side=LEFT)
        self.fenster.mainloop()
App()

        
            

        

