#----------------------------------------------------------------
# Dateiname: Heilpflanze
# Definition einer Klasse, die Heilpflanzen modelliert.
#----------------------------------------------------------------

class Heilpflanze:
    def __init__(self, name, wirkungen):                #1
        self.name = name
        self.wirkungen = list(wirkungen)                #2
        
    def __gt__(self, other):                            #3 
        return len(self.wirkungen) > len(other.wirkungen) 
    
   
    def hat_wirkung(self, wirkung):
        return wirkung in self.wirkungen                #4
        

if __name__ == '__main__':
    a = Heilpflanze('Arnika', ['wundheilend', 'schmerzstillend'])
    b = Heilpflanze('Arnika', ['beruhigend'])
    print(a > b)
    print(a.hat_wirkung('schmerzstillend'))

        

