#----------------------------------------------
# Dateiname: wuerfeln_logo.pyw
# Simulation eines Würfelspiels
# Schaltflächen mit Bildern statt Text
#---------------------------------------------

'''
Die Spielidee:
Man würfelt und addiert in Gedanken die gewürfelten Zahlen. Man versucht, so
nahe wie möglich an die Zahl 21 zu kommen. Wenn die Summe jedoch über 21
liegt, hat man verloren. Das Label mit den Zahlen wird dann gelb.

Die GUI enthält ein Label und zwei Schaltflächen mit Bildsymbolen (Würfel und
Putzeimer).
• Das Label zeigt die bisher gewürfelten Zahlen an.
• Wenn die Schaltfläche mit dem Würfel angeklickt wird, wird eine
Zufallszahl zwischen 1 und 6 gewählt und hinter die bereits „gewürfelten“
Zahlen auf das Label geschrieben.
• Wenn auf die Schaltfläche mit dem Putzeimer geklickt wird, werden die
Zahlen auf dem Label gelöscht.
'''



import tkinter as tk
from random import randint

def wuerfeln():
    global summe # summe wird in der Funktion verändert, daher global
    text = label.cget('text')
    zahl = randint(1, 6)
    summe += zahl
    label.config(text=text + ' ' + str(zahl))
    if summe > 21:
        label.config(bg='yellow')  

def loeschen():
    global summe
    summe = 0
    label.config(text='', bg='white')
 
summe = 0

fenster = tk.Tk()
bild_wuerfel = tk.PhotoImage(file='wuerfel_logo.png')
bild_loeschen = tk.PhotoImage(file='loeschen_logo.png')
label = tk.Label(master=fenster, width=16,
              font=('Arial', 30), text='', bg='white')            
b_wuerfeln = tk.Button(master=fenster, image=bild_wuerfel,
                   command=wuerfeln)
b_loeschen = tk.Button(master=fenster, image=bild_loeschen,
                   command=loeschen)
label.pack()
b_wuerfeln.pack(side=tk.LEFT, padx=30, pady=10)
b_loeschen.pack(side=tk.RIGHT, padx=30, pady=10)
fenster.mainloop()


