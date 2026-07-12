#----------------------------------------------------------------
# Dateiname: bilderquiz.pyw
# Städtequiz. Das Programm zeigt Fotos, man muss raten
# aus welcher Stadt das Bild stammt.
# Autor: Michael Weigend
# Python für Studium und Ausbildung
# Kapitel 12
# Letzte Änderung: 21.2.2022
#----------------------------------------------------------------

from multiprocessing import context
from tkinter import Label, Button, Tk, StringVar, Radiobutton, LEFT, W, BOTH
from urllib.request import urlopen
from PIL import Image, ImageTk
from random import shuffle, choice
import ssl

# Erlaube das Laden von HTTPS-Inhalten
ssl._create_default_https_context = ssl._create_unverified_context
stream = urlopen(url, context=context)

FARBE = '#79b'
BREITE = 400
STÄDTE = [('https://upload.wikimedia.org/wikipedia/commons/2/25/Museo_Bode%2C_Berl%C3%ADn%2C_Alemania%2C_2016-04-22%2C_DD_30.jpg',
           'Berlin'),
          ('https://upload.wikimedia.org/wikipedia/commons/7/72/North_view_of_Charles_Bridge_from_M%C3%A1nes%C5%AFv_most%2C_Prague_20160808_1.jpg',
           'Prag'),
          ('https://upload.wikimedia.org/wikipedia/commons/9/97/Palace_of_Westminster%2C_London_-_Feb_2007.jpg',
           'London'),
          ('https://upload.wikimedia.org/wikipedia/commons/9/94/Atomium%2C_Br%C3%BCssel_1.jpg',
           'Brüssel')]
                    
def optionen(richtig):
    falsch = [stadt for url, stadt in STÄDTE
              if stadt != richtig]
    shuffle(falsch)
    optionenliste = [richtig, falsch[0], falsch[1]]
    shuffle(optionenliste)
    return optionenliste
    
def neue_frage():
    global bild_tk, richtig
    url, richtig = choice(STÄDTE)
    print(url)       #
    opt = optionen(richtig)
    print(opt)
    for i in range(3):
        rb[i].config(text=opt[i], value=opt[i])
    rb[0].select()
    stream = urlopen(url)
    bild_pil = Image.open(stream)
    breite, höhe = bild_pil.size
    b, h = BREITE, int(BREITE/breite*höhe)
    bild_pil = bild_pil.resize(size=(b, h))
    print(b, h)
    bild_tk = ImageTk.PhotoImage(bild_pil)
    label_bild.config(image=bild_tk)
    label_lösung.config(text='???', bg=FARBE)
             
def zeige_lösung():
    if antwort.get() == richtig:
        label_lösung.config(text=richtig, bg='green')
    else:
        label_lösung.config(text=richtig, bg='red')
          
# Widgets
fenster = Tk()
fenster.config(bg=FARBE)
antwort = StringVar()

label_top = Label(master=fenster, bg=FARBE, text='Städtequiz',
                 font=('Impact', 30), fg='white')
label_bild = Label(master=fenster, bg=FARBE)
label_lösung = Label(master=fenster, font=('Arial', 14),
                    width=20, bg=FARBE, fg='white')
rb =[]
for i in range(3):
    rb.append(Radiobutton(master=fenster, bg=FARBE,
                          variable=antwort,
                          command=zeige_lösung,
                          font=('Arial', 14)))
button_neu = Button(master=fenster,text='Neues Bild',
                font=('Arial', 14),
                command=neue_frage)
# Layout
label_top.pack()
label_bild.pack(padx=10, pady=10)
label_lösung.pack()
for radiobutton in rb:
     radiobutton.pack(anchor=W,padx=20)
button_neu.pack(side=LEFT, padx=20, pady=10)

# Start
neue_frage()
