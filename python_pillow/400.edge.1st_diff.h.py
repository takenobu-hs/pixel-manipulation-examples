
from PIL import Image


# im1 = Image.open('../images/img001.png').convert('RGB')
# im1 = Image.open('../images/img001.png').convert('L')
im1 = Image.open('../images/img002.png').convert('L')
width, height = im1.size
# im3 = Image.new('RGB', (width, height))
im3 = Image.new('L', (width, height))

#-- filter coeff
k = [ 0, 0, 0,
     -1, 1, 0,
      0, 0, 0 ]

#-- canvas loop
for y in range(1, height-1):
    for x in range(1, width-1):

        #-- filter window
        win = []
        for wy in [y-1, y, y+1]:
          for wx in [x-1, x, x+1]:
              win.append(im1.getpixel((wx, wy)))

        #-- filter
        s = 0
        for ix, iy in zip(win, k):
          s = s + ix * iy

        s = s + 128
        im3.putpixel((x, y), s)

im3.save('z121.png')


