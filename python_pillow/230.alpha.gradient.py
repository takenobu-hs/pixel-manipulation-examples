
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size
im2 = Image.new('RGBA', (width, height))


#-- pixel operation
for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = r
        g2 = g
        b2 = b
        a = int( (x / width) * 255 )

        im2.putpixel((x, y), (r2, g2, b2, a))


#-- save to png
im2.save('z230.png')

