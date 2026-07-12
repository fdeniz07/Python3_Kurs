# Beispiel 5: Bild mit Text und Farben gestalten
# Dieses Beispiel zeigt, wie du einem Bild Text hinzufügst und verschiedene Farben verwendest.

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import PIL
print(PIL.__version__)

ordner = Path(__file__).parent  # Ordner des Skripts wird ermittelt
bild = Image.new("RGB", (400, 220), color="white")  # Neues Bild mit weißem Hintergrund wird erzeugt
draw = ImageDraw.Draw(bild)  # Zeichenobjekt für das Bild wird erstellt

draw.rectangle((30, 30, 370, 190), outline="green", width=4)  # Grün umrandetes Rechteck wird gezeichnet
draw.ellipse((80, 60, 160, 140), fill="red")  # Roter Kreis wird gezeichnet
draw.rectangle((220, 70, 330, 150), fill="blue")  # Blaues Rechteck wird gezeichnet

try:
    font = ImageFont.truetype("DejaVuSans.ttf", 24)  # Schriftart wird geladen
except OSError:
    font = ImageFont.load_default()  # Fallback-Schriftart wird verwendet

x = bild.width // 2
y = bild.height // 2

draw.text(
    (x, 205),
    "Hallo Python",
    font=font,
    fill="black",
    anchor="mm"
)  # Text wird auf das Bild gesetzt
ziel = ordner / "bild_mit_text.png"  # Zielpfad für das Bild wird festgelegt
bild.save(ziel)  # Bild wird gespeichert
bild.show()  # Bild wird direkt angezeigt
print(f"Bild mit Text gespeichert unter {ziel}")
