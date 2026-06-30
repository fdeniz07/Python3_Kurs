'''
Aufgabe: Systemumgebung
Du sollst ein Python-Skript schreiben, das folgende Funktionen ausführt:

a) Erstelle eine Funktion erstelle_verzeichnis, die als Argument einen Verzeichnisnamen (String) nimmt. 
Die Funktion soll mithilfe des os-Moduls überprüfen, ob das Verzeichnis bereits existiert. Falls nicht, 
soll das Verzeichnis erstellt werden. Gib eine Bestätigung aus, dass das Verzeichnis erstellt wurde oder bereits existiert.

b) Erstelle eine Funktion speichere_text_in_datei, die zwei Argumente nimmt: den Dateinamen (String) 
und den zu speichernden Text (String). Die Funktion soll den Text in der angegebenen Datei speichern. 
Verwende die with-Anweisung, um die Datei zu öffnen und sicherzustellen, dass sie korrekt geschlossen wird.

c) Erstelle eine Funktion lese_datei, die als Argument einen Dateinamen (String) nimmt 
und den Inhalt der Datei ausgibt. Fange mögliche Ausnahmen ab, die beim Versuch, die Datei zu lesen, 
auftreten können (z.B. wenn die Datei nicht existiert), und gib eine entsprechende Fehlermeldung aus.

d) Erstelle eine Funktion liste_dateien_in_verzeichnis, die als Argument einen Verzeichnisnamen (String) nimmt 
und alle Dateien in diesem Verzeichnis auflistet. Verwende das os-Modul, um auf das Dateisystem zuzugreifen.

e) Schreibe ein Hauptprogramm, das die Funktionen in folgender Reihenfolge aufruft: erstelle_verzeichnis 
mit dem Verzeichnisnamen "MeineDaten", speichere_text_in_datei mit einem beliebigen Text 
in einer Datei namens "beispiel.txt" im Verzeichnis "MeineDaten", lese_datei für "beispiel.txt" 
und liste_dateien_in_verzeichnis für das Verzeichnis "MeineDaten". 
'''



import os


# a) Verzeichnis erstellen
def erstelle_verzeichnis(verzeichnisname):
    if not os.path.exists(verzeichnisname):
        os.mkdir(verzeichnisname)
        print(f"Das Verzeichnis '{verzeichnisname}' wurde erstellt.")
    else:
        print(f"Das Verzeichnis '{verzeichnisname}' existiert bereits.")


# b) Text in Datei speichern
def speichere_text_in_datei(dateiname, text):
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(text)
    print(f"Der Text wurde in '{dateiname}' gespeichert.")


# c) Datei lesen
def lese_datei(dateiname):
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            inhalt = datei.read()
            print("\nDateiinhalt:")
            print(inhalt)
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
    except Exception as fehler:
        print(f"Ein Fehler ist aufgetreten: {fehler}")


# d) Dateien im Verzeichnis auflisten
def liste_dateien_in_verzeichnis(verzeichnisname):
    print(f"\nDateien im Verzeichnis '{verzeichnisname}':")

    for eintrag in os.listdir(verzeichnisname):
        pfad = os.path.join(verzeichnisname, eintrag)

        if os.path.isfile(pfad):
            print(eintrag)


# e) Hauptprogramm
verzeichnis = "MeineDaten"
dateiname = os.path.join(verzeichnis, "beispiel1.txt")

erstelle_verzeichnis(verzeichnis)

speichere_text_in_datei(
    dateiname,
    "Dies ist ein Beispieltext für die Python-Aufgabe."
)

lese_datei(dateiname)

liste_dateien_in_verzeichnis(verzeichnis)