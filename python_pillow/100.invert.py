
from PIL import Image

im = Image.open('../images/img001.png').convert('RGB')
width, height = im.size
# print(width, height)


for y in range(height):
    for x in range(width):
        r, g, b = im.getpixel((x, y))

        r = 255 - r
        g = 255 - g
        b = 255 - b

#       im.putpixel((x, y), (r, g, b, 0))
        im.putpixel((x, y), (r, g, b))

im.save('z100.png')


