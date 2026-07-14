#----------------------------------------------------------------
# Dateiname: abrechnung.pyw
# Das objektorientierte Programm ermöglicht das Eingeben und
# von Geldbeträgen in verachiedenen Währungen und. Beim Klick auf die
# Schaltfläche 'Abrechnen' wird die Summe berechnet.
#---------------------------------------------------------------
#abrechnung.pyw
from geld import Geld
from tkinter import Button, Tk, Text, LEFT, END

class App():
    def __init__(self):
        self.fenster = Tk()
        self.text = Text(master=self.fenster,
                          width=30, height=6)
        self.button = Button(master=self.fenster,
                             text='Abrechnen',
                             command=self.abrechnen)
        
        self.text.pack()
        self.button.pack(side=LEFT, padx=5, pady=5)
        self.fenster.mainloop()

    def abrechnen(self):
        text = self.text.get(1.0, END)
        zeilen = text.split('\n')
        summe = Geld('EUR', 0)
        for z in zeilen:
            try:
                währung, betrag = z.split()
                summe = summe + Geld(währung, betrag)
            except:
                pass
        self.text.insert(END, '\n\nSumme: ' + str(summe))
        
App()
        
'''
Beispiel Eingabe:
EUR 100
USD 50
GBP 20
JPY 1000

Kalkulation:
EUR 100 = 100,00 EUR --> 100.00€
USD 50 = 40,77 EUR (50 × 0.8154) --> 40.77€
GBP 20 = 22,258 EUR (20 × 1.1129) --> 22.26€
JPY 1000 = 7,90 EUR (1000 × 0.0079) --> 7.90€
Summe: 100 + 40.77 + 22.26 + 7.90 = 170.93€

Ausgabe:
Summe: EUR 170.93
'''
   

        

