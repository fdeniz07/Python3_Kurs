#---------------------------------------------
# Dateiname: plattform.py
# Gibt die Plattform und Version des Python-Interpreters aus
#---------------------------------------------
import sys
print('Ihre Systemplattform ist',sys.platform)
print('Python-Version:')
print('Python '+ sys.version)

if sys.platform == 'win32':
    from winsound import Beep
    Beep(770, 1000) # Beep mit 770 Hz für 1000 ms (1 Sekunde)

