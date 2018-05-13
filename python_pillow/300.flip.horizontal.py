
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size
im2 = Image.new('RGB', (width, height))


#-- pixel operation
for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = r
        g2 = g
        b2 = b
        x2 = width - x - 1
        y2 = height - y - 1

        im2.putpixel((x2, y2), (r2, g2, b2))

#-- save to png
im2.save('z300.png')

