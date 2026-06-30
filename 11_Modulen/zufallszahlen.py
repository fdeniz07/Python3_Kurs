# zufallszahlen.py
#---------------------------------------------
# Dateiname: zufallszahlen.py
# Änderung der Standardausgabe
#---------------------------------------------

import sys, random
original_stdout = sys.stdout
with open('zahlen.txt', 'w') as sys.stdout:
    print('Zufallszahlen zwischen 1 und 1000')
    for i in range(5):
        print(i, random.randint(1, 1000))
sys.stdout = original_stdout
print('Zufallszahlen wurden in eine Datei geschrieben.')
