#---------------------------------------------
# Dateiname: motivator.py
# Beim Klick auf die Schaltfläche
# erscheint ein neuer Zufallstext auf dem Label.
#---------------------------------------------
from tkinter import Tk, Label, Button
from random import choice
SPRÜCHE = [
            'Du siehst heute gut aus.',
            'Du schaffst es!',
            'Heute ist dein Tag!',
            'Alles wird gelingen!'
          ]                                  #1

def auswählen():                             #2
    text = choice(SPRÜCHE)                   #3
    label.config(text=text)                  #4

fenster = Tk()                               #5
button = Button(master=fenster,
                text='Neue Motivation',
                command=auswählen)           #6
label = Label(master=fenster, width=25,
              height=2, font=('Arial', 16),
              text=SPRÜCHE[0])               #7
label.pack()                                 #8
button.pack()
fenster.mainloop()  
