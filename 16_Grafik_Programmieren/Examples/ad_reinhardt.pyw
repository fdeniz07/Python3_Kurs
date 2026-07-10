#---------------------------------------------
# Dateiname: ad_reinhardt.pyw
# Erzeugt automatisch ein zufälliges Bild aus Rechtecken
#---------------------------------------------
from canvasvg import saveall # https://pypi.org/project/canvasvg/ --> pip install canvasvg
from tkinter import *
from random import choice
from time import asctime

def neue_farbe():
    z = '0123456789ABCDEF'
    return '#' + choice(z) + choice(z) + choice(z)

def malen():
    global id0, id1, id2

    id0 = bild.create_rectangle(0,0,250,300,
                                fill=neue_farbe(),
                                outline='')
    id1 = bild.create_rectangle(100,0,150,300,
                                fill=neue_farbe(),
                                outline='')
    id2 = bild.create_rectangle(0,100,250,200,
                                fill=neue_farbe(),
                                outline='')

def löschen():
    bild.delete(id0)
    bild.delete(id1)
    bild.delete(id2)

def speichern():
    zeitstempel=asctime()
    for ch in ':. ':
        zeitstempel = zeitstempel.replace(ch, '')
    saveall('bild'+zeitstempel+'.svg', bild)
    

fenster = Tk()
button_malen = Button(master=fenster,
                     text='Malen', command=malen)
button_löschen = Button(master=fenster,
                       text='Löschen',command=löschen)
button_speichern = Button(master=fenster,
                       text='Speichern',command=speichern)

bild = Canvas(master=fenster,
              width = 250, height = 300)
bild.pack()
button_malen.pack(side=LEFT)
button_löschen.pack(side=LEFT)
button_speichern.pack(side=LEFT)
fenster.mainloop()
