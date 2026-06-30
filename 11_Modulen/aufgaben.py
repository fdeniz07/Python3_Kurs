import os, time

v1 = [i for i in os.listdir()
      if os.path.isdir(i)]
# C: Alle Unterverzeichnisse im aktuellen
# Arbeitsverzeichnis

v2 = [i for i in os.listdir()
      if time.time() - os.path.getatime(i) > 3600]
# D: Alle Dateien im aktuellen Arbeitsverzeichnis,
# auf die innerhalb der letzten Stunde zugegriffen wurde

v3 = [i for i in os.listdir()
      if i.endswith('.jpg') and os.path.isfile(i)]
# A: Alle JPEG-Bilddateien im aktuellen Arbeitsverzeichnis

v4 = [i[0] for i in os.walk('.')]
# B: Alle Verzeichnisse (relative Pfade) im Verzeichnisbaum,
# dessen Wurzel das aktuelle Arbeitsverzeichnis ist