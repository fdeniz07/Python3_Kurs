# Dateiname: geld_basis.py
# Klasse Geld - Basisversion
#----------------------------------------------------

class Geld:
    wechselkurs ={'USD':0.8154,
                  'GBP':1.1129,
                  'EUR':1.0,
                  'JPY':0.0079} 
   
    def __init__(self, währung, betrag):
        self.währung = währung
        self.betrag = betrag
    def berechneEuro(self):           
        return self.betrag * self.wechselkurs[self.währung]
      
    def add (self, geld):            
        a = self.berechneEuro()
        b = geld.berechneEuro()
        summe = (a + b)/self.wechselkurs[self.währung]
        return Geld(self.währung, summe)
