# ---------------------------------------------------
# Dateiname: geld_erweitert.py
# Klasse Geld mit __add__ und __str__
# -------------------
 
class Geld:
    'Die Klasse modelliert Geldbeträge'
    wechselkurs ={'USD':0.8154,
                  'GBP':1.1129,
                  'EUR':1.0,
                  'JPY':0.0079} 

    def __init__(self, währung, betrag): 
        self.währung = währung
        self.betrag = betrag
    
    def berechneEuro(self):                          
        return self.betrag*self.wechselkurs[self.währung]

    def __add__ (self, geld):                         
        a = self.berechneEuro()
        b = geld.berechneEuro()
        summe = (a + b)/self.wechselkurs[self.währung]
        return Geld(self.währung, summe)

    def __lt__(self, geld):
        a = self.berechneEuro () 
        b = geld.berechneEuro ()
        return a < b
    
    def __str__(self):
        return "{:.2f} {}".format(self.betrag, self.währung)

    def __mul__(self, x):
        ergebnis = self.betrag * x
        return Geld(self.währung, ergebnis)

    def __bool__(self):
        return self.betrag != 0









