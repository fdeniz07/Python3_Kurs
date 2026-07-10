#----------------------------------------------------
# Dateiname:  qsort.py 
# Modul mit Funktion quicksort(), die eine Liste sortiert
# und ihre Arbeitsweise selbst dokumentiert.
#----------------------------------------------------------------


from random import randint
def quicksort(s):
  if len(s) <= 1: # Liste ist bereits sortiert
      return s
  else:
      pivot = s[0]
      s1 = [x for x in s[1:] if x < pivot] # Liste der Elemente kleiner als pivot
      s2 = [x for x in s[1:] if x >= pivot] # Liste der Elemente größer oder gleich pivot
      if __name__ == '__main__': # Nur wenn das Modul direkt ausgeführt wird, werden die Zwischenergebnisse ausgegeben
        print ("Ich sortiere: ", s)
        print('Aufspaltung:', s1, pivot, s2)
      
      return quicksort(s1) + [pivot] +  quicksort(s2) # Rekursiver Aufruf der Funktion für die beiden Teillisten und Zusammenfügen der Ergebnisse

if __name__== '__main__':                              
    s = [17, 7, 85, 15, 11, 20, 9, 5, 87]  
    print ('Sortierte Liste:', quicksort(s))
    input()











                    
