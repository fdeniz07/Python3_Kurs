# Beispiel 3: Farben und Filter ausprobieren
# Dieses Beispiel zeigt, wie du ein Bild in Graustufen verwandeln und spiegeln kannst.

from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


ordner = Path(__file__).parent  # Ordner des Skripts wird ermittelt
bild = Image.new("RGB", (300, 200), color="white")  # Neues Bild mit weißem Hintergrund wird erzeugt
draw = ImageDraw.Draw(bild)  # Zeichenobjekt für das Bild wird erstellt

draw.rectangle((40, 40, 260, 160), fill="lightblue", outline="darkblue", width=4)  # Ein blaues Rechteck wird gezeichnet
draw.ellipse((90, 60, 210, 140), fill="orange")  # Eine orangefarbene Ellipse wird gezeichnet
draw.text((80, 170), "Filter-Beispiel", fill="black")  # Text wird auf das Bild gesetzt

graustufen = ImageOps.grayscale(bild)  # Das Bild wird in Graustufen umgewandelt
spiegeln = ImageOps.mirror(bild)  # Das Bild wird gespiegelt

ziel_graustufen = ordner / "graustufen.png"  # Zielpfad für das Graustufenbild wird festgelegt
ziel_spiegeln = ordner / "spiegeln.png"  # Zielpfad für das gespiegelte Bild wird festgelegt

graustufen.save(ziel_graustufen)  # Graustufenbild wird gespeichert
graustufen.show()  # Graustufenbild wird direkt angezeigt
spiegeln.save(ziel_spiegeln)  # Gespiegeltes Bild wird gespeichert
spiegeln.show()  # Gespiegeltes Bild wird direkt angezeigt

print(f"Graustufen-Bild gespeichert unter {ziel_graustufen}")
print(f"Spiegelbild gespeichert unter {ziel_spiegeln}")
