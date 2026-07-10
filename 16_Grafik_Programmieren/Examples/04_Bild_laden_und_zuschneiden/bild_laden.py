# Beispiel 4: Bild laden und zuschneiden
# Dieses Beispiel zeigt, wie du ein vorhandenes Bild öffnest, zuschneidest und neu speicherst.

from pathlib import Path

from PIL import Image, ImageDraw


ordner = Path(__file__).parent  # Ordner des Skripts wird ermittelt
quelle = ordner / "foto.jpg"  # Pfad zum Quellbild wird festgelegt
ziel = ordner / "foto_zugeschnitten.jpg"  # Pfad für das zugeschnittene Bild wird festgelegt

if not quelle.exists():
    basis = Image.new("RGB", (400, 250), color="lightgray")  # Neues Basisbild wird erzeugt
    draw = ImageDraw.Draw(basis)  # Zeichenobjekt wird erstellt
    draw.rectangle((40, 40, 360, 210), fill="lightblue", outline="darkblue", width=4)  # Hintergrundrechteck wird gezeichnet
    draw.ellipse((120, 70, 280, 180), fill="orange")  # Kreis wird gezeichnet
    draw.text((90, 215), "Beispielbild", fill="black")  # Text wird hinzugefügt
    basis.save(quelle)  # Basisbild wird gespeichert
    print(f"Beispielbild erzeugt unter {quelle}")

bild = Image.open(quelle)  # Quellbild wird geöffnet
# Zuschneiden: links, oben, rechts, unten
zugeschnitten = bild.crop((180, 160, 400, 300))  # Bild wird zugeschnitten
zugeschnitten.save(ziel)  # Zugeschnittenes Bild wird gespeichert
zugeschnitten.show()  # Zugeschnittenes Bild wird direkt angezeigt
print(f"Zugeschnittenes Bild gespeichert unter {ziel}")
