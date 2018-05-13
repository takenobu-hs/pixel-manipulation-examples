
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size
#im2 = Image.new('RGB', (width, height))


#-- pixel operation
Th = 100 * 3
Hi = 255
Lo = 0

for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        sum = r + g + b
        bin = Hi if sum > Th else Lo
        r2 = bin
        g2 = bin
        b2 = bin

        im.putpixel((x, y), (r2, g2, b2))

#-- save to png
im.save('z212b.png')

