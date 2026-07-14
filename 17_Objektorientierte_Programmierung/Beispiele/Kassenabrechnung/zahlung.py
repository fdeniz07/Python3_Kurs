# ---------------------------------------------------
# Dateiname: zahlung.py
# Klasse Zahlung
#----------------------------------------------------
# zahlung.py
from geld import Geld
class Zahlung(Geld):
    'Die Klasse modelliert eine Zahlung mit Datum'
    def __init__(self, währung, betrag, zeitpunkt):
        Geld.__init__(self, währung, betrag)
        self.zeitpunkt = zeitpunkt
   
    def __str__(self):
        return "{} {} Datum: {}".format(self.währung,
                                 round(self.betrag, 2),
                                 self.zeitpunkt)

if __name__ == '__main__':
    from time import asctime
    a = Zahlung('EUR', 10, asctime() )
    b = Geld('USD', 1)
    print(a)
    print(a + b)
   

