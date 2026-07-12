#----------------------------------------------------------------
# Dateiname: graustufen.pyw
# Umwandlung eines Farbbildes in ein Schwarzweißbild.
#----------------------------------------------------------------

''''
Projekt: Graustufen
Das Programm erzeugt aus einem Farbfoto ein Graustufenbild, das mit drei
Farben auskommt: Schwarz, Grau und Weiß. Die Grundidee des Algorithmus:
• Von jedem Pixel des Farbbilds wird die Helligkeit geprüft.
• Es gibt zwei Schwellenwerte: S1 und S2.
• Liegt die Helligkeit unter S1, wird das Pixel schwarz.
• Liegt die Helligkeit zwischen S1 und S2, wird das Pixel grau.
• Liegt die Helligkeit über S2, wird das Pixel weiß.
Wenn die Schwellenwerte geschickt gewählt werden, kann eine interessante
Grafik entstehen. Statt Graustufen können auch andere Farben gewählt werden.
Experimentiere damit!
'''


import tkinter as tk
from tkinter import Tk, Button, Label, PhotoImage, X
DATEINAME = 'gesicht.png'
S1, S2 = 255, 510
def bearbeiten():                                         #1                               
    for x in range (bild.width()):                        #2
        for y in range (bild.height()):
            c = bild.get(x, y)                            #3
            helligkeit = sum(c)                           #4
            if helligkeit < S1:
                bild.put('black', (x, y))
            elif helligkeit < S2:
                bild.put('grey', (x, y))
            else:
                bild.put('white', (x, y))
           

fenster = Tk()
bild = PhotoImage(file=DATEINAME)   
button = Button(master=fenster, command=bearbeiten,
                font=('Arial', 14),
                text='Bearbeiten')        

label = Label(master=fenster, image=bild)                                                  
label.pack()                                          
button.pack(fill=X)  
fenster.mainloop()           


