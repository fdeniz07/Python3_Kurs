# ==========================================
# Tkinter Übung
# Aufgabe: Grafische Benutzeroberfläche
#
# Dieses Programm erstellt ein einfaches
# Tkinter-Fenster mit einem Label und
# einem Button.
#
# Beim Klicken auf den Button wird der
# Text des Labels geändert.
# ==========================================
'''
Aufgabe: Grafische Benutzeroberfläche
Entwickle ein Python-Programm, das ein Tkinter-Anwendungsfenster mit einer grafischen Benutzeroberfläche erstellt. Dein Programm soll folgende Elemente beinhalten und Funktionen ausführen:

a) Importiere das Tkinter-Modul korrekt und initialisiere das Hauptfenster der Anwendung. Benenne das Fenster als "Mein GUI".

b) Füge ein Label-Widget hinzu, das den Text "Willkommen zu deinem GUI!" in der Schriftart "Arial", Größe 16, in blauer Schrift auf gelbem Hintergrund anzeigt. Positioniere das Label zentral im Fenster.

c) Erstelle eine Schaltfläche (Button), die beschriftet ist mit "Klick mich!". Wenn der Button geklickt wird, soll der Text des Labels zu "Button wurde geklickt!" geändert werden. Achte darauf, dass die Schaltfläche und das Label gut sichtbar und nicht übereinander angeordnet sind.

d) Implementiere eine Funktion, die aufgerufen wird, wenn der Button geklickt wird und die den Text des Labels ändert. Verwende die Methode config des Label-Widgets, um den Text zu aktualisieren.

e) Stelle sicher, dass das Fenster eine feste Größe hat und nicht vom Benutzer in der Größe verändert werden kann.

f) Das Programm soll in einer Endlosschleife laufen, sodass das Fenster offen bleibt, bis der Benutzer es manuell schließt. 
'''




import tkinter as tk


# Funktion zum Ändern des Label-Textes
def button_geklickt():
    label.config(text="Button wurde geklickt!")


# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Mein erstes GUI")

# Feste Fenstergröße
fenster.geometry("500x250")
fenster.resizable(False, False)

# Label erstellen
label = tk.Label(
    fenster,
    text="Willkommen zu deinem ersten GUI!",
    font=("Arial", 16),
    fg="blue",
    bg="yellow",
    width=30,
    pady=10
)

label.pack(pady=40)  # Abstand(Vertikaler) nach oben und unten zum Fensterrand

# Button erstellen
button = tk.Button(
    fenster,
    text="Klick mich!",
    font=("Arial", 12),
    command=button_geklickt
)

button.pack(pady=10)  # Vertikaler Abstand zum Label

# Endlosschleife starten
fenster.mainloop()