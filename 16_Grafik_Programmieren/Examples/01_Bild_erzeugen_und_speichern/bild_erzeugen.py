# Beispiel 1: Bild erzeugen und speichern
# Dieses Beispiel zeigt, wie du mit Pillow ein neues Bild erzeugen und als Datei speichern kannst.

from pathlib import Path

from PIL import Image, ImageDraw


ordner = Path(__file__).parent # Legt den Ordner fest, in dem das aktuelle Skript gespeichert ist
bild = Image.new("RGB", (400, 250), color="lightblue") # Erzeugt ein neues Bild mit den Abmessungen 400x250 Pixel und einem hellblauen Hintergrund
draw = ImageDraw.Draw(bild) # Erstellt ein Zeichenobjekt, mit dem du auf dem Bild zeichnen kannst

draw.rectangle((50, 50, 350, 200), outline="darkblue", width=5) # Zeichnet ein Rechteck auf dem Bild mit den angegebenen Koordinaten und einer dunkelblauen Umrandung
draw.ellipse((120, 80, 280, 180), fill="yellow", outline="orange", width=3) # Zeichnet eine Ellipse (Kreis) auf dem Bild mit den angegebenen Koordinaten, einer gelben Füllung und einer orangefarbenen Umrandung
draw.text((90, 210), "Erstellt mit Pillow", fill="black") # Fügt Text auf dem Bild hinzu an den angegebenen Koordinaten mit schwarzer Farbe

ziel_pfad = ordner / "beispiel_bild.png" # Legt den Pfad fest, unter dem das Bild gespeichert werden soll
bild.save(ziel_pfad) # Speichert das Bild unter dem festgelegten Pfad
bild.show() # Öffnet das Bild direkt nach dem Speichern im Standardbildbetrachter

print(f"Bild gespeichert unter {ziel_pfad}")
