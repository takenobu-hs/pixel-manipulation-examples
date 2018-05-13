
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size


#-- pixel operation
for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = g
        g2 = b
        b2 = r

        im.putpixel((x, y), (r2, g2, b2))


#-- save to png
im.save('z204.png')

