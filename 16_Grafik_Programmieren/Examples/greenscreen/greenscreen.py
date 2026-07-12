#----------------------------------------------------------------
# Dateiname: greenscreen.pyw
# Kombiniert zwei Bilder mit der Greesnscreen-Methode.
#----------------------------------------------------------------

'''
Das folgende Programm erzeugt einen Canvas mit weißem Hintergrund und
einer blauen Kreisfläche in der Mitte.
'''

from PIL import Image
BACKGROUND_FILE = 'landschaft.jpg'
PERSON_FILE = 'person.jpg'

im_background = Image.open(BACKGROUND_FILE)                 #1
im_person = Image.open(PERSON_FILE)
list_person = list(im_person.get_flattened_data())                    #2
list_mask = [
    0 if g > 0.9 * (r + b) else 255
    for r, g, b in list_person
]                  #3
im_mask = Image.new(mode = 'L', size=im_person.size)        #4
im_mask.putdata(list_mask)                                  #5
im_background.paste(im_person, box=(100,10), mask=im_mask)  #6
im_background.save("ergebnis.png")
print("Bild wurde gespeichert.")
im_background.show()



