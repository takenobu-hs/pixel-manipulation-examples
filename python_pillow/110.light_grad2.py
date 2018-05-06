
from PIL import Image


im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size
im2 = Image.new('RGB', (width, height))

for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        l = int( (x / width) * 255 )
        r2 = r + l
        g2 = g + l
        b2 = b + l

        im2.putpixel((x, y), (r2, g2, b2))

im2.save('z110.png')


