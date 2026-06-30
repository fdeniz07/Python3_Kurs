#---------------------------------------------
# Dateiname: verzeichnisse.py
# Unterverzeichnisse ausgeben
#---------------------------------------------

import os
print('Unterverzeichnisse:')
inhalt = os.listdir()
for item in inhalt:
    if os.path.isdir(item):
        print(item)


