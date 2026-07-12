#----------------------------------------------------------------
# Dateiname: farbstufen_1.pyw
# Erzeugt ein zweifarbiges Bild
#----------------------------------------------------------------
from PIL import Image
FILE = 'katze.jpg'                                     #1
im = Image.open(FILE)                                  #2
width, height = im.size                                #3
for x in range(width):                                 #4
    for y in range(height):
        pixel =  im.getpixel((x, y))
        if sum(pixel) < 350:                           
            im.putpixel((x, y), (200, 0, 0))           #5
        else:
            im.putpixel((x, y), (200, 200, 255))       #6

im.show()                                              #7                                      
                                      




