# Beispiel 2: Bild verkleinern und drehen
# Dieses Beispiel zeigt, wie du ein Bild verkleinern und anschließend drehen kannst.

from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


ordner = Path(__file__).parent  # Ordner des Skripts wird ermittelt
bild = Image.new("RGB", (300, 200), color="white")  # Neues Bild mit weißem Hintergrund wird erzeugt
draw = ImageDraw.Draw(bild)  # Zeichenobjekt für das Bild wird erstellt

draw.rectangle((60, 40, 240, 160), fill="red", outline="black", width=3)  # Ein rotes Rechteck wird gezeichnet
draw.circle((150, 100), 40, fill="yellow")  # Ein gelber Kreis wird gezeichnet

groesse = (150, 100)  # Neue Größe für die Verkleinerung wird festgelegt
verkleinert = bild.resize(groesse)  # Das Bild wird verkleinert
drehen = ImageOps.exif_transpose(verkleinert.rotate(25))  # Das verkleinerte Bild wird um 25 Grad gedreht

ziel_pfad = ordner / "bild_verarbeitet.png"  # Zielpfad für das Ergebnis wird festgelegt
drehen.save(ziel_pfad)  # Das veränderte Bild wird gespeichert
drehen.show()  # Das Ergebnis wird direkt angezeigt
print(f"Verarbeitetes Bild gespeichert unter {ziel_pfad}")
