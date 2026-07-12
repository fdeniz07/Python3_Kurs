# Beispiel 6: Bild komprimieren und speichern
# Dieses Beispiel zeigt, wie du ein Bild in einer anderen Qualität speicherst.

# Beispiel: Bild komprimieren und Vergleich erstellen

from pathlib import Path
import os

from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, filedialog

ordner = Path(__file__).parent

# Dateiauswahlfenster ausblenden
Tk().withdraw()

# Bild auswählen
datei = filedialog.askopenfilename(
    title="Bild auswählen",
    filetypes=[
        ("Bilddateien", "*.jpg *.jpeg *.png"),
        ("Alle Dateien", "*.*")
    ]
)

if datei:

    bild = Image.open(datei)
    pfad = Path(datei)

    # Dateinamen
    # original_datei = pfad.with_name(f"{pfad.stem}_original.jpg")
    # komprimiert_datei = pfad.with_name(f"{pfad.stem}_komprimiert.jpg")
    # vergleich_datei = pfad.with_name(f"{pfad.stem}_vergleich.jpg")
    # Dateinamen im Ordner des Programms
    original_datei = ordner / "bild_original.jpg"
    komprimiert_datei = ordner / "bild_komprimiert.jpg"
    vergleich_datei = ordner / "bild_vergleich.jpg"

    # Original und komprimiertes Bild speichern
    bild.save(original_datei, quality=100)
    bild.save(komprimiert_datei, quality=30)

    # Bilder öffnen
    original = Image.open(original_datei)
    komprimiert = Image.open(komprimiert_datei)

    # Vergleichsbild erstellen
    abstand = 20
    beschriftung = 40

    breite = original.width + komprimiert.width + abstand
    hoehe = max(original.height, komprimiert.height) + beschriftung

    vergleich = Image.new("RGB", (breite, hoehe), "white")
    draw = ImageDraw.Draw(vergleich)

    # Bilder einfügen
    vergleich.paste(original, (0, beschriftung))
    vergleich.paste(komprimiert, (original.width + abstand, beschriftung))

    # Schrift laden
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except OSError:
        font = ImageFont.load_default()

    # Überschriften
    draw.text(
        (original.width // 2, 20),
        "Original",
        fill="black",
        font=font,
        anchor="mm"
    )

    draw.text(
        (original.width + abstand + komprimiert.width // 2, 20),
        "Komprimiert (Quality = 30)",
        fill="black",
        font=font,
        anchor="mm"
    )

    # Vergleich speichern
    vergleich.save(vergleich_datei)

    # Vergleich anzeigen
    vergleich.show()

    # Dateigrößen
    print(f"Original:      {os.path.getsize(original_datei):,} Byte")
    print(f"Komprimiert:   {os.path.getsize(komprimiert_datei):,} Byte")
    print(f"Vergleich:     {os.path.getsize(vergleich_datei):,} Byte")

    print("\nDateien wurden gespeichert:")
    print(original_datei)
    print(komprimiert_datei)
    print(vergleich_datei)