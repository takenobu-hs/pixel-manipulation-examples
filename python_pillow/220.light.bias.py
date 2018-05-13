
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size


#-- pixel operation
s   = 70
upr = 255

for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = min(r + s, upr)
        g2 = min(g + s, upr)
        b2 = min(b + s, upr)

        im.putpixel((x, y), (r2, g2, b2))


#-- save to png
im.save('z220.png')

