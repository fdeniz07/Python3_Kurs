# ---------------------------------------------------
# Dateiname: geld.py
# Klasse Geld mit __add__ und __str__
#----------------------------------------------------

class Geld:
    'Die Klasse modelliert Geldbeträge'
    wechselkurs ={'USD':0.8154,
                  'GBP':1.1129,
                  'EUR':1.0,
                  'JPY':0.0079} 

    def __init__(self, währung, betrag): 
        self.währung = währung
        self.betrag = float(betrag)
    
    def berechneEuro(self):                         #1
        return self.betrag*self.wechselkurs[self.währung]

    def __add__ (self, geld):                        #2
        a = self.berechneEuro()
        b = geld.berechneEuro()
        summe = (a + b)/self.wechselkurs[self.währung]
        return Geld(self.währung, summe)
       
    def __str__(self):
        return "{} {}".format(self.währung, round(self.betrag, 2))

if __name__ == '__main__':
    a = Geld('EUR', 10)
    b = Geld('USD', 1)
    print(a + b)  
   

