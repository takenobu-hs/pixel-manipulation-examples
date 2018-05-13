
from PIL import Image


#-- read pixels
im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size


#-- pixel operation
for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r = 255 - r
        g = 255 - g
        b = 255 - b

        im.putpixel((x, y), (r, g, b))


#-- save to png
im.save('z200.png')

