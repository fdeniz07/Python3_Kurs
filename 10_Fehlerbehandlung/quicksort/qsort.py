#----------------------------------------------------------------
# Dateiname: qsort.py
# Schnelles Sortieren mit Quicksort
#----------------------------------------------------------------
def quicksort(s):
  if len(s) <= 1:
      return s
  else:
      pivot = s[0]
      s1 = [x for x in s[1:] if x < pivot]
      s2 = [x for x in s[1:] if x >= pivot]     
      return quicksort(s1) + [pivot] +  quicksort(s2)

if __name__== '__main__':                              
    s = [17, 7, 85, 15, 11, 20, 9, 5, 87]  
    print ('Sortierte Liste:', quicksort(s))
 











                    
