
from PIL import Image


im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size

s   = 70
upr = 255

for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r2 = min(r + s, upr)
        g2 = min(g + s, upr)
        b2 = min(b + s, upr)

        im.putpixel((x, y), (r2, g2, b2))

im.save('z105.png')


