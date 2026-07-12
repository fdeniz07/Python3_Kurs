#----------------------------------------------------------------
# Dateiname: flasche.py
# Objektorientierte Modellierung einer Flasche
#----------------------------------------------------------------
class Flasche:                                       #1                         
    "Klasse modelliert eine Flasche"                 #2
    def __init__ (self, fassungsvermögen=1000):      #3                      
       self.inhalt = 0                               #4
       self.max_inhalt = fassungsvermögen
       self.geöffnet = False

    def öffnen(self):                            
       self.geöffnet = True

    def schließen(self):
        self.geöffnet = False

    def füllen(self, volumen):
        if self.geöffnet:
            if self.inhalt + volumen <= self.max_inhalt:
                self.inhalt += volumen
    def leeren(self):
        "Flasche komplett entleeren"
        if self.geöffnet:
            self.inhalt = 0
