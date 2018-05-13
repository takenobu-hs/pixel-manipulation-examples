
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size


#-- pixel operation
Th = 100
Hi = 255
Lo = 0

for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = Hi if r > Th else Lo
        g2 = Hi if g > Th else Lo
        b2 = Hi if b > Th else Lo

        im.putpixel((x, y), (r2, g2, b2))


#-- save to png
im.save('z212.png')

