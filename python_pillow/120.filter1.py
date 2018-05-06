
from PIL import Image


# im1 = Image.open('../images/img001.png').convert('RGB')
im1 = Image.open('../images/img001.png').convert('L')
width, height = im1.size
# im3 = Image.new('RGB', (width, height))
im3 = Image.new('L', (width, height))

k = [ 0, 0, 0,
      0, 1, 0,
      0, 0, 0 ]

for y in range(1, height-1):
    for x in range(1, width-1):

        win = []
        for wy in [y-1, y, y+1]:
          for wx in [x-1, x, x+1]:
              win.append(im1.getpixel((wx, wy)))

        s = 0
        for ix, iy in zip(win, k):
          s = s + ix * iy

        im3.putpixel((x, y), s)

im3.save('z120.png')


