
from PIL import Image


#-- read pixels
im1 = Image.open('../images/img001.png').convert('RGB')
width, height = im1.size
im2 = Image.open('../images/img002.png').convert('RGB')
im3 = Image.new('RGB', (width, height))


#-- pixel operation
a = 0.7

for y in range(height):
    for x in range(width):
        r1, g1, b1 = im1.getpixel((x, y))
        r2, g2, b2 = im2.getpixel((x, y))

        r3 = int( r1*a + r2*(1-a) )
        g3 = int( g1*a + g2*(1-a) )
        b3 = int( b1*a + b2*(1-a) )

        im3.putpixel((x, y), (r3, g3, b3))

#-- save to png
im3.save('z231.png')

