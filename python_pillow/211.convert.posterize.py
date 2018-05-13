
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size


#-- pixel operation
q = 32

for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = int(r / q) * q
        g2 = int(g / q) * q
        b2 = int(b / q) * q

        im.putpixel((x, y), (r2, g2, b2))


#-- save to png
im.save('z211.png')

