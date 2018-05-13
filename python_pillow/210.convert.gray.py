
from PIL import Image


im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size


for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        gray = int((r + g + b) / 3)
        r2 = gray
        g2 = gray
        b2 = gray

        im.putpixel((x, y), (r2, g2, b2))

im.save('z102.png')


